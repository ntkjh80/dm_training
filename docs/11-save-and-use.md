# 11. 저장한 모델 사용하기

## 어댑터와 병합본의 차이

| 저장물 | 들어 있는 것 | 사용할 때 |
| --- | --- | --- |
| adapter 폴더 | 추가 가중치, head와 보정 정보 등 | 기반 모델도 필요하므로 함께 관리 |
| merged 폴더 | 추가 가중치를 합친 전체 모델 | 파일과 임시 메모리 사용량이 커짐 |
| metrics.json | 설정, 평가 값, 예제 응답 | 성능과 실행 조건 확인 |
| environment.txt | 학습한 환경의 패키지 목록 | 다음 실행의 재현 자료 |

동봉 코드는 adapter를 기본 저장합니다. --save-merged를 추가하면 병합본도 만듭니다. 예를 들어 4B의 16비트 가중치는 단순 산술만으로도 약 8GB이며, 구성 파일과 임시 작업 공간은 별도입니다. 저장 실패를 학습 실패와 혼동하지 말고 남은 디스크와 메모리를 확인합니다.

근거: [9. FastDecisionModel과 DecisionTrainer 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/decision.py)

## 가장 단순한 재사용은 같은 환경에서 불러오기

```bash
python predict_saved.py outputs/course/adapter
python predict_saved.py outputs/course/adapter --state "환불 규정만 알려주세요."
```

기반 모델 다운로드가 캐시에 없다면 다시 필요할 수 있습니다. Mac과 CUDA 환경 사이로 옮길 때는 의존성, 기반 모델, head, 보정 파일의 호환성을 함께 확인합니다. weights 파일 하나만 골라 복사하지 않습니다.

## Decision API로 연결하기

GUI로 학습했다면 API 설정에서 실행 이름을 선택합니다. 코드로 만든 병합본은 원문의 방식대로 모델 폴더를 지정해 Studio를 시작할 수 있습니다. 아래는 지원되는 GPU 실행 환경에서의 예입니다.

```bash
UNSLOTH_SYSTEMONE_MODEL=/절대경로/merged \
  unsloth studio -H 127.0.0.1 -p 8888
```

Windows PowerShell에서는 $env:UNSLOTH_SYSTEMONE_MODEL="C:\경로\merged"를 먼저 설정하고 Studio 명령을 실행합니다. Settings의 Decision API를 켠 다음 call_api.py로 확인합니다. 원문의 병합 모델 서빙 경로는 GPU를 요구하므로 CPU Laya 실행과 같은 조건으로 생각하면 안 됩니다.

근거: [1. 원문 학습 안내](https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth)

## Mac과 CPU에서 내보낸 모델을 실행할 때

최신 소스에는 일부 Decision 모델의 GGUF 내보내기도 있습니다. 지원 구조와 전용 실행기가 필요합니다. 일반 채팅용 GGUF 변환이나 Ollama 등록만으로 head와 확률 처리가 유지된다고 가정하지 않습니다. Mac에서는 먼저 같은 MLX 환경의 predict_saved.py로 확인하고, 앱이 제공하는 내보내기와 Decision API 지원 조합을 차례로 점검합니다.

근거: [10. Apple Silicon Decision 학습 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/decision_mlx.py) · [16. Decision GGUF 내보내기 구현](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/export/decision.py)

---

[전체 목차](../README.md) · [이전 장](10-python-colab.md) · [다음 장](12-troubleshooting.md)
