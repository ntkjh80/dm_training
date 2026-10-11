"""Teaching workflow based on the documented Unsloth public API.

No model weights are bundled. --check-data uses only the Python standard library.
Training needs a compatible Unsloth environment and GPU; hardware training has
not been executed as part of this course preparation.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def read_rows(path):
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path.name}:{number}: invalid JSON: {exc}") from exc
    if not rows:
        raise ValueError(f"Empty dataset: {path}")
    return rows

def validate_splits(splits):
    """Validate the hard-label subset used in this introductory course."""
    states, groups, ids = {}, {}, set()
    for split, rows in splits.items():
        counts = Counter()
        for i, row in enumerate(rows, 1):
            where = f"{split} row {i}"
            if not isinstance(row, dict):
                raise ValueError(f"{where}: expected an object")
            state, questions, gold = (row.get(k) for k in ("state", "questions", "gold"))
            if not isinstance(state, str) or not state.strip():
                raise ValueError(f"{where}: nonempty text state required")
            key = " ".join(state.split())
            if key in states:
                raise ValueError(f"{where}: duplicate state, previously in {states[key]}")
            states[key] = split
            if not isinstance(questions, dict) or not questions or not isinstance(gold, dict):
                raise ValueError(f"{where}: questions and gold must be objects")
            if set(questions) != set(gold):
                raise ValueError(f"{where}: question and gold names differ")
            if "id" in row:
                if row["id"] in ids:
                    raise ValueError(f"{where}: duplicate id")
                ids.add(row["id"])
            if row.get("group_id") is not None:
                group = str(row["group_id"])
                if group in groups and groups[group] != split:
                    raise ValueError(f"{where}: group {group} leaks across splits")
                groups[group] = split
            for name, q in questions.items():
                if not isinstance(q, dict) or not q.get("instructions"):
                    raise ValueError(f"{where}/{name}: instructions required")
                kind, label, criteria = q.get("type"), gold[name], q.get("criteria")
                if kind == "choice":
                    valid = isinstance(criteria, dict) and len(criteria) >= 2 and isinstance(label, str) and label in criteria
                elif kind == "noul":
                    valid = type(label) is bool
                elif kind == "score":
                    valid = isinstance(criteria, list) and len(criteria) >= 2 and type(label) is int and 0 <= label < len(criteria)
                else:
                    valid = False
                if not valid:
                    raise ValueError(f"{where}/{name}: invalid {kind} label or criteria")
                counts[f"{name}={label}"] += 1
        print(f"{split}: {len(rows)} rows; label counts: {dict(counts)}")

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data-dir", type=Path, default=ROOT / "data")
    p.add_argument("--output", type=Path, default=ROOT / "outputs" / "demo")
    p.add_argument("--model", default="unsloth/Qwen3.5-0.8B")
    p.add_argument("--revision", help="Optional exact Hugging Face model revision")
    p.add_argument("--epochs", type=float, default=2)
    p.add_argument("--max-steps", type=int, default=0, help="Positive value overrides epochs")
    p.add_argument("--batch-size", type=int, default=1)
    p.add_argument("--accumulation", type=int, default=8)
    p.add_argument("--max-seq-length", type=int, default=1024)
    p.add_argument("--learning-rate", type=float, default=2e-4)
    p.add_argument("--save-merged", action="store_true")
    p.add_argument("--check-data", action="store_true")
    args = p.parse_args()
    if min(args.epochs, args.batch_size, args.accumulation, args.max_seq_length, args.learning_rate) <= 0 or args.max_steps < 0:
        p.error("Training values must be positive; max-steps must be nonnegative.")
    splits = {name: read_rows(args.data_dir / f"{name}.jsonl") for name in ("train", "calibration", "test")}
    validate_splits(splits)
    if args.check_data:
        print("PASS: local schema, hard labels, exact duplicates and group split checks.")
        print("This does not check semantic label quality or near-duplicate leakage.")
        return
    if args.output.exists() and any(args.output.iterdir()):
        p.error("Output folder is not empty. Choose a new --output to preserve earlier runs.")

    # Unsloth must be imported before transformers and torch.
    from unsloth import FastDecisionModel, DecisionTrainer, is_bfloat16_supported
    import torch
    from transformers import TrainingArguments

    apple = platform.system() == "Darwin" and platform.machine() == "arm64"
    if not apple and (not torch.cuda.is_available() or torch.version.hip is not None):
        p.error("This teaching script targets Apple Silicon MLX or NVIDIA CUDA. Use vendor-specific Studio setup for AMD/Intel, or Colab.")
    args.output.mkdir(parents=True, exist_ok=True)
    kwargs = {"revision": args.revision} if args.revision else {}
    model, tokenizer = FastDecisionModel.from_pretrained(
        model_name=args.model, decision_head="clef", max_seq_length=args.max_seq_length,
        load_in_4bit=True, random_state=3407, **kwargs)
    model = FastDecisionModel.get_peft_model(
        model, r=16, lora_alpha=16, lora_dropout=0,
        use_gradient_checkpointing="unsloth", random_state=3407)
    items, reports = {}, {}
    for name, rows in splits.items():
        items[name], reports[name] = FastDecisionModel.build_dataset(rows, tokenizer, model)
        print(name, reports[name])
        if not items[name] or reports[name]["skipped"]:
            raise RuntimeError(f"Fix all skipped or empty data before training: {name}")
    baseline = FastDecisionModel.evaluate(model, tokenizer, items["calibration"], batch_size=1)
    bf16 = not apple and is_bfloat16_supported()
    # On old GPUs such as T4, avoid forcing pure fp16 for Qwen3.5.
    # Current Unsloth may select its float32 fallback; that uses more memory/time.
    schedule = {"max_steps": args.max_steps} if args.max_steps else {"num_train_epochs": args.epochs}
    trainer = DecisionTrainer(
        model=model, processing_class=tokenizer,
        train_dataset=items["train"], eval_dataset=items["calibration"],
        head_learning_rate=1e-4,
        args=TrainingArguments(
            output_dir=str(args.output / "checkpoints"),
            per_device_train_batch_size=args.batch_size, per_device_eval_batch_size=1,
            gradient_accumulation_steps=args.accumulation,
            learning_rate=args.learning_rate, warmup_steps=1,
            lr_scheduler_type="cosine", weight_decay=0.01,
            bf16=bool(bf16), fp16=False, eval_strategy="epoch",
            save_strategy="no", logging_steps=1, report_to="none", seed=3407,
            **schedule))
    result = trainer.train()
    calibrated = FastDecisionModel.calibrate(model, tokenizer, items["calibration"], batch_size=1)
    test = FastDecisionModel.evaluate(model, tokenizer, items["test"], batch_size=1)
    model.save_pretrained(str(args.output / "adapter"))
    if args.save_merged:
        model.save_pretrained_merged(str(args.output / "merged"))
    FastDecisionModel.for_inference(model)
    answers = FastDecisionModel.predict(model, tokenizer,
        "중복 결제 금액을 오늘 돌려주세요.",
        splits["train"][0]["questions"])
    metadata = {"created_utc": datetime.now(timezone.utc).isoformat(),
        "platform": platform.platform(), "backend": "MLX" if apple else "CUDA",
        "arguments": vars(args), "data_reports": reports,
        "calibration_before_training": baseline, "calibration_after_fitting": calibrated,
        "final_test": test, "train_metrics": result.metrics, "example_prediction": answers,
        "packages": {}, "data_sha256": {}}
    for name in ("unsloth", "unsloth_zoo", "transformers", "torch", "mlx"):
        try:
            metadata["packages"][name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            pass
    for name in splits:
        metadata["data_sha256"][name] = hashlib.sha256((args.data_dir / f"{name}.jsonl").read_bytes()).hexdigest()
    (args.output / "metrics.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    frozen = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True)
    if frozen.returncode == 0:
        (args.output / "environment.txt").write_text(frozen.stdout, encoding="utf-8")
    print(json.dumps({"test": test, "prediction": answers}, ensure_ascii=False, indent=2, default=str))
    print("Saved:", args.output)
    print("Teaching data is synthetic and small. These numbers are not production performance.")

if __name__ == "__main__":
    main()
