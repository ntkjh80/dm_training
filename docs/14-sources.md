# 14. 출처와 변경 확인

아래 링크는 2026년 10월 11일 확인한 공식 문서와 공개 구현입니다. 앱 화면과 지원 모델은 바뀔 수 있으므로 실습 전 해당 설치 안내와 노트북을 확인합니다. 본문 속 숫자는 출처의 보고값, 계산 예시, 교육용 제안을 구분해 표시했습니다.

[1. 원문 학습 안내](https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth)

[2. 로컬 Decision API와 Laya](https://unsloth.ai/docs/models/decision-laya)

[3. Windows 설치](https://unsloth.ai/docs/get-started/install/windows-installation)

[4. Mac 설치](https://unsloth.ai/docs/get-started/install/mac)

[5. Linux 설치](https://unsloth.ai/docs/get-started/install/linux)

[6. Studio 설치와 하드웨어 조건](https://unsloth.ai/docs/new/studio/install)

[7. 공식 Qwen3.5 Decision 노트북](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_%284B%29-Decision.ipynb)

[8. typed decisions 데이터 설명](https://huggingface.co/datasets/LocalLLaMA/typed-decisions)

[9. FastDecisionModel과 DecisionTrainer 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/decision.py)

[10. Apple Silicon Decision 학습 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/decision_mlx.py)

[11. 정답과 확률 처리 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/_decision_common.py)

[12. 확률 보정의 의미](https://scikit-learn.org/stable/modules/calibration.html)

[13. Colab 자원 제한 안내](https://research.google.com/colaboratory/faq.html)

[14. AMD 설치](https://unsloth.ai/docs/get-started/install/amd)

[15. Intel GPU 설치](https://unsloth.ai/docs/get-started/install/intel)

[16. Decision GGUF 내보내기 구현](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/export/decision.py)

## 공식 소스 확인 기준

공개 저장소 main 확인 시점의 커밋 식별자: 0acf8b171731f11be19db7680e6273b664528639. main은 계속 바뀌므로 재현 실험에서는 실제 설치한 버전과 모델 리비전을 별도로 기록합니다.

학습 안내 페이지의 설정과 노트북의 설정은 동일하지 않습니다. 교재 [4장](04-source-benchmarks.md)의 비교를 보고 자신이 실행한 값을 기록하세요. 본 교재의 고객 문의 문장과 강의 활동은 교육용으로 새로 구성했습니다.

---

[전체 목차](../README.md) · [이전 장](13-completion-checklist.md)
