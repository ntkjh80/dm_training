# 실습 시작 안내

[전체 목차](../README.md) · [PC별 경로](../docs/05-pc-environments.md) · [60분 강의 대본](../docs/teaching-script.md)

기준일: 2026-10-11. 모든 명령은 특별한 설명이 없으면 이 `practice` 폴더에서 실행합니다. Windows는 보통 `python`, Mac/Linux는 환경에 따라 `python3`를 사용합니다. 아래는 준비된 가상환경의 `python`을 기준으로 합니다.

## 1. 어떤 실습부터 할까?

| 목표 | 필요한 것 | 순서 |
| --- | --- | --- |
| 데이터 형식 이해 | Python | 2절 데이터 점검 → 8절 내 데이터 만들기 |
| 내 PC에서 판단 결과 보기 | Unsloth Desktop/Studio, Laya | 3절 설치 → 7절 API 호출 |
| NVIDIA PC에서 학습 | 지원 NVIDIA GPU와 CUDA 환경 | 3절 → 4절 환경 확인 → 5절 학습 |
| Apple Silicon Mac에서 학습 | arm64 Python과 최신 MLX 환경 | 3절 → 4절 환경 확인 → 5절 학습 |
| Intel Mac 또는 GPU 없는 PC에서 학습 | 브라우저와 Colab GPU | 9절 Colab |
| AMD/Intel GPU에서 학습 | 지원 GPU, 벤더별 패키지 | 3절의 공식 설치 안내 → Studio 소량 학습 |

제공 예제 48건은 교육용 가상 사례입니다. 모델 파일, 앱 설치 파일, API 키는 저장소에 포함하지 않습니다.

## 2. 외부 패키지 없이 데이터 점검

저장소 최상위 폴더에서 한 번 이동합니다. 이미 `practice` 안에 있다면 첫 줄은 생략합니다.

```bash
cd practice
python train_decision.py --check-data
```

Python 표준 라이브러리만 사용합니다. 마지막에 `PASS`가 표시되면 파일 형식과 입문용 확정 라벨 검사를 통과한 것입니다.

| 파일 | 원문 수 | 질문 수 | 용도 |
| --- | --- | --- | --- |
| [data/train.jsonl](data/train.jsonl) | 24 | 72 | 모델 학습 |
| [data/calibration.jsonl](data/calibration.jsonl) | 12 | 36 | 학습 중 평가와 확률 보정 |
| [data/test.jsonl](data/test.jsonl) | 12 | 36 | 마지막 시험 |

질문과 정답 이름, 선택지 키, 참거짓·정수 타입, 중복 원문을 검사합니다. 동일 `group_id`가 서로 다른 묶음에 섞이면 중단합니다. 뜻이 비슷한 중복, 정답 품질, 실제 고객 대화 단위 분리는 사람이 확인해야 합니다. 실제 실험에서 모델 선택을 반복한다면 검증용과 보정용 자료를 추가로 분리하세요.

## 3. PC별 설치 경로

처음에는 [Unsloth Desktop 다운로드](https://unsloth.ai/download)에서 자신의 운영체제용 앱을 설치하는 경로가 간단합니다. 앱의 초기 환경 구성이 끝난 뒤 GPU 인식 상태를 확인합니다. 브라우저형 Studio를 직접 설치하는 방법은 [교재 6장](../docs/06-installation.md)에 있습니다.

Desktop/Studio 내부 환경과 현재 터미널의 Python은 다를 수 있습니다. Python 코드 실습은 아래 **공식 Core 설치 안내로 준비한 환경**에서 실행합니다. Python 3.12를 권장 기준으로 삼되 설치 안내의 현재 요구사항을 확인합니다.

| 환경 | 공식 안내 | 설치 후 진행 |
| --- | --- | --- |
| Windows + NVIDIA | [Windows 설치](https://unsloth.ai/docs/get-started/install/windows-installation) | GPU 드라이버와 CUDA 인식 확인 → Studio 또는 동봉 코드 |
| Linux + NVIDIA | [Linux 설치](https://unsloth.ai/docs/get-started/install/linux) | GPU 드라이버와 CUDA 인식 확인 → Studio 또는 동봉 코드 |
| Apple Silicon Mac | [Mac 설치](https://unsloth.ai/docs/get-started/install/mac) | arm64 Python과 최신 MLX/Unsloth 환경 확인 → 작은 모델 |
| Intel Mac | [Mac 설치 안내](https://unsloth.ai/docs/get-started/install/mac), [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_%284B%29-Decision.ipynb) | Laya CPU 추론 체험 → 학습은 Colab GPU부터 |
| GPU 없는 Windows/Linux | [Studio 안내](https://unsloth.ai/docs/new/studio/install), [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_%284B%29-Decision.ipynb) | Laya CPU 추론 체험 → 학습은 Colab GPU부터 |
| AMD GPU | [AMD 설치](https://unsloth.ai/docs/get-started/install/amd) | 지원 GPU·OS·ROCm 조합 확인 → Studio에서 소량 검증 |
| Intel GPU | [Intel 설치](https://unsloth.ai/docs/get-started/install/intel) | 지원 GPU·XPU 조합 확인 → Studio에서 소량 검증 |

동봉 학습 코드는 NVIDIA CUDA와 Apple Silicon MLX를 대상으로 합니다. AMD/Intel에는 해당 벤더의 설치 환경에서 Studio 경로를 사용하세요. 일반 학습 지원 여부만으로 모든 Decision 모델의 양자화·저장 조합까지 지원된다고 판단하지 않습니다.

## 4. 현재 터미널의 환경 확인

공통 확인:

```bash
python -c "import sys; print(sys.executable)"
python -m pip show unsloth unsloth-zoo
python -c "from unsloth import FastDecisionModel, DecisionTrainer; print('Decision API import OK')"
```

`Decision API import OK`가 나타나지 않으면 실행 중인 Python과 패키지 환경을 먼저 맞춥니다.

NVIDIA 환경에서 추가 확인:

```bash
nvidia-smi
python -c "import torch; print(torch.cuda.is_available()); print(torch.version.cuda)"
```

첫 명령에서 GPU가 보이고 두 번째 명령에서 CUDA 사용 가능 여부가 `True`로 나오는지 확인합니다. 시스템 RAM과 GPU 전용 메모리는 다릅니다.

Apple Silicon에서 추가 확인:

```bash
python -c "import platform; print(platform.machine())"
python -c "import mlx.core as mx; print(mx.default_device())"
```

`arm64` Python과 최신 MLX/`unsloth-zoo`가 필요합니다. Core 패키지의 MLX 경로는 PyTorch도 요구합니다. 의존성 오류가 나면 현재 공식 설치 안내를 다시 적용합니다. CUDA용 패키지를 Mac에 설치하거나 AMD/XPU 환경을 일반 CUDA 패키지로 덮어쓰지 않습니다.

로컬 코드 환경 준비가 어렵다면 9절의 공식 Colab 설치 셀을 이용할 수 있습니다.

## 5. 학습 실행

설치 확인을 통과한 환경에서 순서대로 실행합니다.

```bash
python train_decision.py --max-steps 5 --output outputs/smoke
python train_decision.py --epochs 2 --output outputs/course
python predict_saved.py outputs/course/adapter
```

두 학습 명령은 각각 기반 모델에서 새로 시작합니다. 5 step은 작동 점검용입니다. 출력 폴더가 이미 존재하고 비어 있지 않으면 중단하므로 새 폴더 이름을 사용하세요.

학습 → 보정 → 최종 시험 → 저장 순서로 진행합니다. 시험 자료는 학습과 보정에 사용하지 않습니다. 실무에서 새로운 실험을 설계하는 방법은 [교재 8장](../docs/08-training-data.md)을 참고하세요.

| 옵션 | 기본값 또는 의미 |
| --- | --- |
| `--model` | `unsloth/Qwen3.5-0.8B` |
| `--revision` | 실제 Hugging Face 모델 리비전을 지정해 기반 모델 버전 고정 |
| `--epochs` | 기본 2회 순회 |
| `--max-steps` | 양수이면 epochs보다 우선 |
| `--batch-size` | 기본 1 |
| `--accumulation` | 기본 8 |
| `--max-seq-length` | 기본 1024 |
| `--learning-rate` | 기본 `2e-4` |
| `--data-dir` | 학습·보정·시험 파일을 담은 폴더 |
| `--output` | 실행 결과를 저장할 새 폴더 |
| `--save-merged` | 어댑터 외에 병합본도 저장; 추가 메모리와 디스크 필요 |

GPU가 bfloat16을 지원하지 않으면 코드에서 fp16을 강제하지 않습니다. T4처럼 float32 경로가 필요한 경우 더 느리고 메모리를 더 사용할 수 있습니다. 원문에 적힌 시간을 내 PC의 소요 시간으로 보장할 수는 없습니다.

## 6. 결과 읽기와 재실행

| 경로 | 내용 |
| --- | --- |
| `outputs/course/adapter/` | 기반 모델에 추가하는 가중치와 Decision 구성 |
| `outputs/course/merged/` | `--save-merged`를 지정한 경우의 전체 모델 |
| `outputs/course/metrics.json` | 지표, 실행 설정, 데이터 해시, 버전, 실제 예제 응답 |
| `outputs/course/environment.txt` | `pip freeze`가 성공한 경우의 패키지 버전 목록 |

지표는 질문 단위입니다. 한 원문에 세 질문이면 판단 수는 세 배입니다.

- `calibration_before_training`: 학습 전 보정용 자료의 평가 결과.
- `calibration_after_fitting`: 확률 보정 단계의 반환값.
- `final_test`: 학습과 보정에 쓰지 않은 최종 시험 자료의 평가 결과.

환불 질문의 시험 정답은 `true` 1건, `false` 11건으로 불균형합니다. 항상 false만 답해도 정확도는 약 91.7%이지만 환불 요청 재현율은 0%입니다. 높은 숫자 하나를 실무 품질로 해석하지 않습니다.

```bash
python predict_saved.py outputs/course/adapter --state "환불 규정만 알려주세요."
```

어댑터는 기반 모델도 필요합니다. 다른 PC로 옮길 때 저장 폴더 전체와 기반 모델, 실행 환경의 호환성을 확인합니다. 병합본과 Decision API 연결은 [교재 11장](../docs/11-save-and-use.md)을 따릅니다.

## 7. 로컬 API 호출

1. Studio의 Settings → API → Decision API를 엽니다.
2. `Serve requests`를 켭니다.
3. 한국어 체험용으로 multilingual Laya를 선택하고 다운로드를 마칩니다.
4. Settings의 Access tokens에서 키를 확인합니다.
5. 키를 현재 터미널의 환경 변수에 넣고 실행합니다.

Mac/Linux:

```bash
export UNSLOTH_API_KEY="여기에_내_API_키"
python3 call_api.py
```

Windows PowerShell:

```powershell
$env:UNSLOTH_API_KEY="여기에_내_API_키"
python call_api.py
```

기본 접속 주소는 `127.0.0.1:8888`입니다. 포트가 다르면 `--port 실제포트`를 추가합니다. 명시적으로 Keyless API access를 켠 localhost 환경에서는 키를 생략할 수 있습니다.

[request.json](request.json)의 `model: "default"`는 앱에서 선택한 모델을 뜻합니다. Python으로 학습한 모델이 자동으로 선택되지는 않습니다. GUI의 실행 모델 선택 또는 [병합본 지정 절차](../docs/11-save-and-use.md)를 거칩니다.

모델이 실제 반환한 선택지와 확률을 기록하세요. 교재의 확률 예시는 실행 결과를 미리 정해 놓은 값이 아닙니다.

## 8. 내 데이터로 바꾸기

원본 예제는 보관하고 별도 폴더에 세 파일을 만듭니다. 저장소 안에 개인 자료를 둔다면 Git 제외 경로인 `private-data/`를 사용할 수 있습니다.

```text
private-data/
├── train.jsonl
├── calibration.jsonl
└── test.jsonl
```

```bash
python train_decision.py --data-dir private-data --check-data
python train_decision.py --data-dir private-data --output outputs/my-course
```

각 질문의 `instructions`, `criteria`를 업무 기준에 맞게 바꾸고 `gold`를 검토합니다. 재실행 때 사용하는 [request.json](request.json)의 질문 정의도 같은 업무 기준으로 맞춥니다. 학습 때의 팀 선택지와 예측 때의 선택지가 다르면 같은 평가를 수행하는 것이 아닙니다.

동봉 검증기는 입문용 확정 라벨을 검사합니다. 공식 API의 모든 확률 라벨 형식을 지원하는 범용 검증기는 아닙니다. 보정 자료와 최종 시험 자료의 수량·대표성도 확인하세요.

[prepare_data.py](prepare_data.py)는 동봉 가상 예제를 만드는 코드입니다. 데이터 파일이 이미 제공되므로 실습 전에 다시 실행할 필요는 없습니다. 기존 파일이 있으면 덮어쓰지 않고 중단합니다.

## 9. GPU 없는 PC에서 Colab 사용

1. [공식 Decision 노트북](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_%284B%29-Decision.ipynb)을 열고 자신의 Drive에 사본을 저장합니다.
2. 런타임 유형을 GPU로 바꾸고 공식 설치 셀을 실행합니다.
3. `train_decision.py`, `predict_saved.py`, `request.json`, `data/`를 업로드해 `/content/practice/` 아래에 둡니다.
4. 아래 노트북 셀로 먼저 형식과 짧은 실행을 확인합니다.

```python
!python /content/practice/train_decision.py --check-data
!python /content/practice/train_decision.py --max-steps 5 --output /content/smoke
```

작동 확인 후 별도 폴더로 전체 절차를 체험합니다.

```python
!python /content/practice/train_decision.py --epochs 2 --output /content/course
!python /content/practice/predict_saved.py /content/course/adapter
```

세션이 끝나기 전에 결과 폴더 전체를 압축해 내려받습니다.

```python
import shutil
from google.colab import files

archive_path = shutil.make_archive("/content/decision-course-result", "zip", "/content/course")
files.download(archive_path)
```

Colab의 무료 GPU 종류와 사용 시간은 보장되지 않습니다. 브라우저가 내 PC에 있어도 학습과 업로드한 데이터 처리는 원격 환경에서 이루어집니다. 상세 조건은 [Colab FAQ](https://research.google.com/colaboratory/faq.html)를 확인하세요.

다운로드한 모델이 모든 CPU PC에서 바로 실행되는 것은 아닙니다. 해당 기반 모델과 head를 지원하는 실행 환경이 필요합니다. CPU의 Laya 체험과 학습한 모델의 GPU 서빙 조건을 구분합니다.

## 10. 검증 범위와 오류 해결

자료 제작 과정에서 Python 문법, 예제 데이터 형식, 공식 gold 변환 규칙과 예제 대조, 잘못된 자료 거부, 모의 API 호출을 점검했습니다. Markdown 전환 후 문서 링크, 파일 구성, 데이터 점검도 통과했습니다.

실제 모델 다운로드, CUDA/MLX 학습, 실제 Unsloth API 추론, 모든 운영체제·드라이버 조합의 설치는 이 자료 제작 과정에서 수행하지 않았습니다. 성능표는 공식 문서 보고값이며 실제 학습 결과를 별도로 만들어 주장하지 않습니다.

문제가 생기면 [오류 해결 교재](../docs/12-troubleshooting.md)를 보고, 실행한 명령·Python 경로·GPU·패키지 버전·오류 메시지를 함께 기록하세요.
