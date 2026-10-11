# 04. 원문 성능표와 학습 설정

원문이 보고한 수치는 아래와 같습니다. 우리 PC에서 측정한 값이 아니며, 표의 VRAM도 모든 설정에 적용되는 최소 사양은 아닙니다.

| 모델 | 표에 적힌 정확도 | VRAM | 학습 시간 |
| --- | --- | --- | --- |
| Qwen3.5 0.8B | 78% | 4GB | 42분 |
| Qwen3.5 2B | 81% | 8GB | 40분 |
| Llama 3.2 3B | 79% | 4.1GB | 30분 |
| Gemma 4 E4B | 77% | 14.4GB | 49분 |
| Laya 추가 학습 | 77% | 2.5GB | 10분 |

원문 첫 표의 typed decisions, BANKING77, CLINC150 결과와 holdout 결과는 서로 다른 평가 범위입니다. 숫자 하나를 모든 한국어 업무의 정확도로 옮겨 쓰지 않습니다. 공식 노트북은 새 head가 붙은 초기 상태를 거의 추측 수준으로 설명하므로, 이 비교를 일반 챗봇의 모든 능력이 학습 전에는 낮다는 뜻으로 읽지 않습니다.

근거: [1. 원문 학습 안내](https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth) · [7. 공식 Qwen3.5 Decision 노트북](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_%284B%29-Decision.ipynb)

## 원문 안의 설정이 서로 다르다

| 위치 | 표시된 값 | 실습에서의 해석 |
| --- | --- | --- |
| 도입 설명 | LoRA rank 64, 1 epoch | 실험 설명 중 한 설정 |
| GUI와 권장 설정 | rank 16, 2 epochs, 2e-4 | 처음 비교할 기준값 |
| 본문 코드 | max_steps 240, 2e-5 | 위 설정과 동일한 실험이 아님 |
| 공식 노트북 | max_steps 60, 2e-4 | 또 다른 실행 예제 |

이 교재의 작은 실습은 batch 1, accumulation 8, 길이 1024로 메모리 부담을 낮춰 시작합니다. 이는 교육용 선택이며 원문 수치 재현 설정은 아닙니다. max_steps를 양수로 정하면 epochs보다 우선합니다. 5 step은 작동 점검용, 2 epochs는 전체 절차 체험용입니다.

## 학습 시간은 PC마다 달라진다

공식 노트북은 Qwen3.5 4B의 60 step을 무료 T4에서 약 2시간, RTX PRO 6000에서 약 12분 수행한 사례를 적고 있습니다. T4의 정밀도 제약으로 float32 경로를 쓰면 느려질 수 있습니다. 다운로드와 설치 시간도 따로 필요합니다. 강의 중 전체 학습 완료를 기다리는 일정은 피하고, 사전 실행 기록을 준비합니다.

근거: [7. 공식 Qwen3.5 Decision 노트북](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_%284B%29-Decision.ipynb)

---

[전체 목차](../README.md) · [이전 장](03-probability-calibration.md) · [다음 장](05-pc-environments.md)
