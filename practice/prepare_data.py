"""Write 48 original Korean teaching examples. These are not a benchmark."""
import json
from pathlib import Path

QUESTIONS = {
    "team": {
        "type": "choice",
        "instructions": "문의의 주된 요청을 담당할 팀 하나를 고르세요.",
        "criteria": {
            "billing": "청구, 결제, 영수증, 환불 요청",
            "technical": "로그인, 오류, 접속, 기능 장애",
            "sales": "구매 전 가격, 견적, 도입, 상품 상담",
            "other": "위 세 팀에 해당하지 않는 문의나 인사",
        },
    },
    "refund": {
        "type": "noul",
        "instructions": "고객이 실제로 돈을 돌려달라고 요청했나요? 환불 규정 질문만 하거나 환불을 원하지 않는다고 하면 아니오입니다.",
    },
    "urgency": {
        "type": "score",
        "instructions": "명시된 처리 시점과 현재 업무 중단을 기준으로 긴급도를 고르세요. 시점 언급이 없으면 1입니다.",
        "criteria": [
            "0 여유 있음: 급하지 않거나 다음 주 이후 처리해도 된다고 명시",
            "1 일반: 시점 언급이 없거나 며칠 이내 답변 요청",
            "2 긴급: 오늘 또는 즉시 처리 요청, 현재 업무나 서비스 중단",
        ],
    },
}

# Deliberately different sentences in each split. Real data should also be split
# by customer, conversation, document family and time, not only by exact text.
EXAMPLES = {
    "train": [
        ("이번 달 요금이 두 번 빠졌습니다. 중복된 금액을 오늘 돌려주세요.", "billing", True, 2),
        ("카드 결제 영수증을 보내주세요.", "billing", False, 1),
        ("결제 취소하고 환불받고 싶습니다. 다음 주에 처리해도 괜찮아요.", "billing", True, 0),
        ("환불받으려는 것은 아닙니다. 환불 규정만 알려주세요.", "billing", False, 1),
        ("계좌로 입금한 이용료를 반환해 주세요.", "billing", True, 1),
        ("청구서 주소 변경을 오늘 마감 전에 부탁드립니다.", "billing", False, 2),
        ("로그인 버튼을 누르면 오류가 나서 지금 일을 못 하고 있습니다.", "technical", False, 2),
        ("프로필 사진 변경 기능이 동작하지 않아요.", "technical", False, 1),
        ("내보내기 버튼 위치를 알려주세요. 급하지 않습니다.", "technical", False, 0),
        ("비밀번호 초기화 메일이 오지 않네요. 며칠 안에 답변 바랍니다.", "technical", False, 1),
        ("현재 전 직원이 접속할 수 없습니다. 즉시 복구해 주세요.", "technical", False, 2),
        ("알림 설정 오류를 확인해 주세요. 다음 달에 해결되어도 됩니다.", "technical", False, 0),
        ("새로 도입할까 합니다. 20명 이용 시 견적이 궁금합니다.", "sales", False, 1),
        ("오늘 구매 결정을 해야 해서 기업 요금 안내를 오늘 부탁드려요.", "sales", False, 2),
        ("학생용 상품 가격을 알려주세요. 급하지 않아요.", "sales", False, 0),
        ("아직 구매 전입니다. 두 요금제 차이를 알려주세요.", "sales", False, 1),
        ("다음 분기에 도입할 예정입니다. 다음 주 이후 상담하면 됩니다.", "sales", False, 0),
        ("구매 상담 예약을 오늘 안에 확정해 주세요.", "sales", False, 2),
        ("친절하게 도와주셔서 감사 인사 남깁니다.", "other", False, 1),
        ("채용 담당 연락처가 궁금합니다.", "other", False, 1),
        ("공개 행사 장소를 다음 주에 알려주셔도 됩니다.", "other", False, 0),
        ("보도자료 담당자 연락처를 오늘 보내주세요.", "other", False, 2),
        ("사무실 방문 가능 시간을 알려주세요. 급한 용건은 아닙니다.", "other", False, 0),
        ("오늘 진행되는 행사 시작 시간을 바로 알려주세요.", "other", False, 2),
    ],
    "calibration": [
        ("연간 이용료를 잘못 결제했습니다. 금액을 환급해 주세요.", "billing", True, 1),
        ("환불은 원치 않고 세금계산서만 오늘 발급해 주세요.", "billing", False, 2),
        ("해지 후 남은 금액을 반환 바랍니다. 서두르지 않으셔도 됩니다.", "billing", True, 0),
        ("화면이 멈춰 현재 주문 처리를 못 합니다.", "technical", False, 2),
        ("검색 기능이 가끔 잘못된 결과를 보여 줍니다.", "technical", False, 1),
        ("테마 색상 설정이 저장되지 않아요. 다음 주에 확인 부탁해요.", "technical", False, 0),
        ("구매하기 전에 할인 적용 조건을 상담하고 싶어요.", "sales", False, 1),
        ("오늘 계약할 예정이니 신규 견적을 즉시 보내주세요.", "sales", False, 2),
        ("도입 예산은 내년에 잡습니다. 다음 달에 상담해 주세요.", "sales", False, 0),
        ("커뮤니티 운영자에게 감사의 말을 전하고 싶습니다.", "other", False, 1),
        ("언론 인터뷰 일정에 오늘 답변이 필요합니다.", "other", False, 2),
        ("봉사 행사 안내를 요청합니다. 급하지 않습니다.", "other", False, 0),
    ],
    "test": [
        ("사용하지 않은 구독료를 돌려받고 싶어요. 오늘 입금 부탁합니다.", "billing", True, 2),
        ("취소할 생각은 없습니다. 청구 내역 확인서를 주세요.", "billing", False, 1),
        ("청구된 부가세 계산 방식이 궁금해요. 답은 다음 주여도 됩니다.", "billing", False, 0),
        ("파일 첨부가 실패합니다. 확인해 주세요.", "technical", False, 1),
        ("전체 서비스가 멈춰 현재 고객 응대를 못 하고 있어요.", "technical", False, 2),
        ("사용자 이름 수정 후 표시가 틀립니다. 급한 문제는 아닙니다.", "technical", False, 0),
        ("처음 가입할 회사입니다. 라이선스 단가를 알려주세요.", "sales", False, 1),
        ("구매 결재가 오늘 끝나므로 신규 견적서를 오늘 보내주세요.", "sales", False, 2),
        ("새 상품 시연을 다음 달에 받아보고 싶습니다. 급하지 않아요.", "sales", False, 0),
        ("홈페이지에 나온 회사 주소를 확인하고 싶습니다.", "other", False, 1),
        ("출입 기자 등록 마감이 오늘이라 담당자 확인을 바로 부탁해요.", "other", False, 2),
        ("지난 행사 사진을 요청합니다. 다음 주 이후 보내주셔도 돼요.", "other", False, 0),
    ],
}

def main():
    root = Path(__file__).resolve().parent
    data = root / "data"
    data.mkdir(exist_ok=True)
    for split, examples in EXAMPLES.items():
        rows = [dict(id=f"{split}-{i:03d}", group_id=f"{split}-{i:03d}",
                     state=state, questions=QUESTIONS,
                     gold={"team": team, "refund": refund, "urgency": urgency})
                for i, (state, team, refund, urgency) in enumerate(examples, 1)]
        path = data / f"{split}.jsonl"
        if path.exists():
            raise SystemExit(f"Already exists; keep your data safe: {path}")
        path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
        print(f"{path.name}: {len(rows)} rows / {len(rows) * 3} decisions")
    request = {"model": "default", "state": "중복 결제된 금액을 오늘 돌려주세요.", "questions": QUESTIONS}
    (root / "request.json").write_text(json.dumps(request, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
