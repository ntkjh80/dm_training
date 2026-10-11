# 10. Python 실습과 Colab 학습

## 설치 없이 먼저 데이터 점검하기

동봉 practice 폴더에서 아래 명령을 실행합니다. Windows는 python, Mac과 Linux는 보통 python3를 사용합니다. 아래 예시는 준비된 가상환경의 python을 사용합니다.

```bash
python train_decision.py --check-data
```

이 단계는 외부 패키지나 모델 다운로드 없이 정답 타입, 질문 이름, 중복 원문, 묶음 간 섞임을 확인합니다. 의미가 비슷한 문장 중복이나 정답 자체의 정확성까지 판정하지는 않습니다.

## 학습 환경에서 실행하기

공식 운영체제별 안내에 따라 Unsloth Core와 해당 GPU용 패키지를 설치한 환경을 활성화합니다. Apple Silicon은 MLX 모듈을 포함한 최신 unsloth와 unsloth-zoo가 필요합니다. NVIDIA용 CUDA 환경에서는 GPU가 PyTorch에 인식되어야 합니다. [실습 시작 안내](../practice/README.md)에 설치 확인 명령이 있습니다.

```bash
python train_decision.py --max-steps 5 --output outputs/smoke
python train_decision.py --epochs 2 --output outputs/course
python predict_saved.py outputs/course/adapter
```

smoke는 기능 점검, course는 별도의 학습 실행입니다. 두 실행 모두 기반 모델에서 새로 시작합니다. 이미 파일이 있는 출력 폴더에는 덮어쓰지 않습니다. 4B를 시도하려면 --model unsloth/Qwen3.5-4B를 추가하되 메모리와 실행 시간을 다시 확인합니다.

코드는 데이터 읽기 → 모델과 head 준비 → 학습 → 별도 보정 → 최종 시험 → 저장 → 새 입력 판단 순서입니다. report에서 skipped가 나오면 중단합니다. metrics.json에 지표와 설정, 파일 해시와 패키지 버전을 남깁니다. 고정한 모델 리비전은 --revision으로 지정할 수 있습니다.

근거: [9. FastDecisionModel과 DecisionTrainer 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/decision.py) · [10. Apple Silicon Decision 학습 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/decision_mlx.py)

## GPU 없는 PC는 Colab으로 학습하기

1. 출처 7의 공식 Colab 노트북을 열고 자신의 Drive에 사본을 저장합니다. 런타임 유형을 GPU로 바꿉니다.
2. 공식 설치 셀을 먼저 실행합니다. 자원 배정이 되지 않으면 사용 가능한 시간대나 다른 지원 환경에서 다시 시도합니다.
3. practice 폴더의 학습 코드와 data 폴더를 Colab에 업로드합니다. /content/practice 아래에 코드와 data가 함께 있도록 배치합니다.
4. 노트북 셀에서 !python /content/practice/train_decision.py --max-steps 5 --output /content/smoke 를 실행합니다. 이후 새 출력 폴더로 정식 체험을 수행합니다.
5. 세션이 끝나기 전에 출력 폴더 전체를 압축해 다운로드합니다. adapter, metrics.json, environment.txt를 함께 보관합니다.

무료 Colab의 GPU 종류와 사용 시간은 보장되지 않습니다. 브라우저가 내 PC에 떠 있어도 계산과 업로드한 자료는 원격 환경에서 처리됩니다. 개인 PC에서만 처리해야 하는 자료는 로컬 경로를 사용하세요.

근거: [7. 공식 Qwen3.5 Decision 노트북](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_%284B%29-Decision.ipynb) · [13. Colab 자원 제한 안내](https://research.google.com/colaboratory/faq.html)

---

[전체 목차](../README.md) · [이전 장](09-studio-training.md) · [다음 장](11-save-and-use.md)
