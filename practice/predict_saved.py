"""Reload a saved decision checkpoint in the same supported training environment."""
import argparse
import json
from pathlib import Path

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("model", help="Path to adapter or merged decision checkpoint")
    p.add_argument("--state", default="중복 결제된 돈을 오늘 돌려주세요.")
    args = p.parse_args()
    from unsloth import FastDecisionModel
    model, tokenizer = FastDecisionModel.from_pretrained(args.model, load_in_4bit=True)
    FastDecisionModel.for_inference(model)
    questions = json.loads(Path(__file__).with_name("request.json").read_text(encoding="utf-8"))["questions"]
    result = FastDecisionModel.predict(model, tokenizer, args.state, questions)
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

if __name__ == "__main__":
    main()
