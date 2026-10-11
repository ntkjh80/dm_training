# 01. 시작하기

**Unsloth로 나만의 Decision 모델 만들기**

개념 설명과 모든 PC 환경을 위한 실습 교재

기준일: 2026-10-11 · 초보자와 실습 진행자를 위한 한국어 자료

Decision 모델은 고객 문의나 문서를 읽고, 우리가 정한 질문에 선택지와 확률로 답하는 모델입니다. 반복되는 분류 작업을 프로그램에 연결하고 싶을 때 유용합니다. 이 교재에서는 한국어 고객 문의를 예로 들어 모델 실행부터 내 데이터 학습, 평가, 저장까지 따라갑니다.

## 먼저 알아둘 결론

이미 학습된 모델을 내 PC에서 실행하는 체험은 가벼운 환경에서도 시작할 수 있습니다. 내 데이터로 모델을 바꾸는 학습은 지원되는 GPU나 Apple Silicon 환경을 준비해야 합니다. PC에 적합한 가속기가 없다면 브라우저에서 Colab GPU로 학습할 수 있습니다.

Unsloth의 접근은 기존 언어 모델에 선택지를 채점하는 작은 판정 모듈을 붙이고, 정답 예제로 조정하는 것입니다. 입력과 여러 질문을 함께 처리하며, 장문의 답변을 생성하는 과정이 필요하지 않습니다. 원문은 GUI와 Python 경로를 모두 제공합니다.

근거: [1. 원문 학습 안내](https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth) · [9. FastDecisionModel과 DecisionTrainer 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/decision.py) · [10. Apple Silicon Decision 학습 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/decision_mlx.py)

## 이 교재를 읽는 순서

| 하고 싶은 일 | 읽을 부분 | 실습 결과 |
| --- | --- | --- |
| 개념부터 이해하기 | [2장](02-decision-model.md)부터 [4장](04-source-benchmarks.md) | 판단 구조와 확률을 설명할 수 있음 |
| 내 PC에서 먼저 실행하기 | [5장](05-pc-environments.md)부터 [7장](07-local-inference.md) | 한국어 입력에 대한 실제 응답 |
| 내 데이터로 학습하기 | [8장](08-training-data.md)부터 [11장](11-save-and-use.md) | 저장한 모델과 평가 기록 |
| 수업을 진행하기 | 별도 강의 대본 | 60분 수업과 선택 실습 30분 |
| 오류를 해결하기 | [12장](12-troubleshooting.md)과 [13장](13-completion-checklist.md) | 설정 점검과 다음 학습 계획 |

## 함께 제공되는 실습 파일

practice 폴더에는 한국어 예제 48건, 로컬 API 호출 코드, 학습과 재실행 코드가 들어 있습니다. 예제는 형식을 익히도록 직접 만든 소량의 가상 데이터이며, 실제 고객 자료나 성능 벤치마크가 아닙니다. 소프트웨어와 모델은 독자가 선택한 환경에 별도로 설치합니다.

**실습의 성공 기준은 데이터가 읽히고, 학습이 완료되고, 저장한 모델을 다시 불러와 답을 얻는 것입니다. 작은 예제에서 높은 정확도가 나오는 것을 실무 투입 기준으로 삼지 않습니다.**

---

[전체 목차](../README.md) · [다음 장](02-decision-model.md)
