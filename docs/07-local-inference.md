# 07. 학습 전에 내 PC에서 판단해 보기

이 단계는 완성된 Laya 모델을 실행해 API 사용법을 익히는 체험입니다. 내 데이터가 모델 가중치를 바꾸는 단계는 [9장](09-studio-training.md)부터입니다.

1. Settings → API → Decision API에서 Serve requests를 켭니다.
2. 한국어 체험에는 multilingual 모델을 선택하고 다운로드를 완료합니다. CPU 실행으로 시작할 수 있습니다.
3. Try It을 열어 state에 “중복 결제된 금액을 오늘 돌려주세요”를 입력합니다.
4. choice 질문으로 담당 팀을 묻고 billing, technical, sales, other를 지정합니다. noul로 환불 요청 여부, score로 긴급도를 추가합니다. 전체 형식은 동봉 request.json에 있습니다.
5. 응답에 나온 선택지와 확률을 읽습니다. 다음에는 “환불은 원하지 않습니다. 규정만 알려주세요”로 바꾸어 부정 표현을 비교합니다.

Laya multilingual의 문서상 크기는 약 678MB이고 최소 RAM 안내는 4GB입니다. 입력 공간은 1024 토큰이므로 긴 문서를 넣기보다 짧은 문장부터 사용합니다. 첫 호출은 모델 로딩 때문에 이후 호출보다 오래 걸릴 수 있습니다.

근거: [2. 로컬 Decision API와 Laya](https://unsloth.ai/docs/models/decision-laya)

## 실습 파일로 API 호출하기

Python이 설치된 터미널에서 practice 폴더로 이동합니다. Settings의 Access tokens에서 확인한 키를 현재 터미널에 설정합니다. 예시 문자열을 실제 키로 바꾸되 코드 파일 안에 저장할 필요는 없습니다.

**macOS 또는 Linux**

```bash
export UNSLOTH_API_KEY="여기에_내_API_키"
python3 call_api.py
```

**Windows PowerShell**

```powershell
$env:UNSLOTH_API_KEY="여기에_내_API_키"
python call_api.py
```

앱의 API 포트가 8888이 아니라면 --port 실제포트를 추가합니다. 코드는 127.0.0.1의 /v1/systemone에 요청하며, 모델 지정 default는 앱에서 선택한 Decision 모델을 가리킵니다. 화면에서 명시적으로 Keyless API access를 켠 환경은 키를 생략할 수 있습니다.

## 답이 달라도 먼저 기록한다

예제에 적힌 정답은 우리가 기대하는 업무 기준입니다. 모델의 실제 숫자는 실행할 때 확인해야 합니다. 학습 전부터 잘 맞히는지, 부정 표현에서 틀리는지, 애매한 입력에서 확률이 낮아지는지를 먼저 모읍니다. 사전 모델로 충분하면 추가 학습을 서두를 필요가 없습니다.

---

[전체 목차](../README.md) · [이전 장](06-installation.md) · [다음 장](08-training-data.md)
