# 14. 출처와 변경 확인

아래는 2026년 10월 11일 확인한 공식 문서·공개 구현과 추가 교육 자료의 출처입니다. 앱 화면과 지원 모델은 바뀔 수 있으므로 실습 전 해당 설치 안내와 노트북을 확인합니다. 본문 속 숫자는 출처의 보고값, 계산 예시, 교육용 제안을 구분해 표시했습니다.

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

## RAG 보강과 추가 읽기

[17. Avi Chawla — RAG vs. Jev + RAG, X 게시물](https://x.com/_avichawla/status/2107767245917368751): 2026-10-07 게시. 본문과 동적 도식을 브라우저에서 확인했습니다.

[18. Avi Chawla — Jev for RAG, clearly explained!](https://blog.dailydoseofds.com/p/jev-for-rag-clearly-explained): 검색·근거 평가·기준 적용·답변 보류의 역할 설명.

[19. Avi Chawla — Jev, Clearly Explained](https://blog.dailydoseofds.com/p/jev-clearly-explained): typed 판단 인터페이스와 판단 오류·보정의 구분.

[20. Avi Chawla — Build your own Jev (100% local)](https://x.com/_avichawla/article/2101563610644496464): 원문에 연결된 아티클. 추가 학습 없이 선택지 토큰을 채점하는 예를 확인했습니다.

[21. SGLang 공식 Native APIs](https://docs.sglang.io/docs/basic_usage/native_api): `/v1/score`와 토큰 점수 API 확인.

[22. LMSYS — Scaling JEV-like Decision Models with SGLang](https://www.lmsys.org/blog/2026-09-25-sglang-decision-models/): 선택지 채점과 보정된 정답 확률의 구분.

15~16장의 한국어 문의 문장, 확률, 기준, 실습 코드는 교육용으로 새로 구성했습니다. 원문의 그림은 해당 게시물에 링크하고, 저장소에는 [자체 제작 도식](../assets/README.md)을 넣었습니다. 두 단계의 순차 API 호출은 첫 필터 결과에 맞춰 입력을 확정하기 위한 이 교재의 구현 선택입니다.

모의 실행과 동작 검사를 수행했지만, Jev·Laya·SGLang의 실제 속도나 RAG 정확도를 비교 측정하지 않았습니다. 다른 글의 성능 배수를 이 저장소의 결과로 사용하지 않습니다.

## 공식 소스 확인 기준

공개 저장소 main 확인 시점의 커밋 식별자: 0acf8b171731f11be19db7680e6273b664528639. main은 계속 바뀌므로 재현 실험에서는 실제 설치한 버전과 모델 리비전을 별도로 기록합니다.

학습 안내 페이지의 설정과 노트북의 설정은 동일하지 않습니다. 교재 [4장](04-source-benchmarks.md)의 비교를 보고 자신이 실행한 값을 기록하세요. 본 교재의 고객 문의 문장과 강의 활동은 교육용으로 새로 구성했습니다.

---

[전체 목차](../README.md) · [이전 장](13-completion-checklist.md) · [다음 장](15-rag-decision-gates.md)
