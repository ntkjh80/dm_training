# 08. 내 데이터를 만드는 방법

한 줄에 JSON 객체 하나를 저장하는 JSONL 형식을 사용합니다. state는 판단할 원문, questions는 질문과 기준, gold는 정답입니다. 다음은 읽기 쉽게 줄을 나눈 예이며, 실제 JSONL 파일에서는 객체 하나를 한 줄로 저장합니다.

```json
{
  "state": "중복 결제된 금액을 오늘 돌려주세요.",
  "questions": {
    "team": {"type": "choice", "instructions": "담당 팀은?",
      "criteria": {"billing": "결제와 환불", "other": "기타"}},
    "refund": {"type": "noul", "instructions": "환불 요청인가?"},
    "urgency": {"type": "score", "instructions": "긴급도는?",
      "criteria": ["여유", "일반", "오늘 또는 즉시"]}
  },
  "gold": {"team": "billing", "refund": true, "urgency": 2}
}
```

choice 정답은 설명 문장이 아닌 선택지 키입니다. noul은 JSON의 true 또는 false이고, score는 0부터 시작하는 단계 번호입니다. 공식 구현은 확률 분포 정답도 받지만 입문 실습은 확정 라벨만 사용합니다. 애매한 사례의 확률을 임의로 꾸며 넣지 않습니다.

근거: [8. typed decisions 데이터 설명](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) · [11. 정답과 확률 처리 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/_decision_common.py)

## 라벨을 붙이기 전에 합의할 기준

“환불 규정을 알려주세요”와 “돈을 돌려주세요”를 구분합니다. 긴급도는 명시된 처리 시점이나 현재 업무 중단으로 정합니다. 담당 팀은 고객의 주된 요청 하나로 고릅니다. 두 사람이 같은 자료를 읽고 다른 답을 고른다면 모델을 학습하기 전에 기준부터 수정합니다.

처음에는 대표 사례와 자주 틀리는 사례를 모아 검토합니다. 교육용 계획 예로 200~500건을 먼저 정리할 수 있지만, 충분한 수량은 클래스 수와 문장 다양성에 따라 달라집니다. 가상 문장을 반복해 늘린 수천 건보다 검토된 실제 사례가 더 유용할 수 있습니다.

## 자료를 나누는 기준

동봉 예제는 학습 24건, 보정 12건, 시험 12건으로 나뉩니다. 1건에 질문 3개가 있어 판단 수는 각각 72개, 36개, 36개입니다. 원문 수와 판단 수를 따로 기록하세요. 같은 고객 대화의 후속 문장이나 복사된 문서가 다른 묶음에 섞이지 않게 합니다.

실무 자료는 고객·대화·문서 묶음과 시점을 기준으로 먼저 분리합니다. 데이터가 충분하다면 검증용과 보정용도 별도로 둡니다. 시험 자료는 모델 선택이나 기준 조절에 사용하지 않고 마지막에 확인합니다.

---

[전체 목차](../README.md) · [이전 장](07-local-inference.md) · [다음 장](09-studio-training.md)
