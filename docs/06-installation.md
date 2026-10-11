# 06. 설치와 첫 실행

## 가장 쉬운 공통 방법

1. 공식 다운로드 페이지에서 자신의 운영체제에 맞는 Unsloth Desktop을 받습니다. Mac은 설치 파일을 열어 Applications로 옮기고, Windows는 설치 프로그램의 안내를 따릅니다. Linux는 공식 Linux 배포 안내를 따릅니다.
2. 앱을 처음 열고 초기 환경 구성이 끝날 때까지 기다립니다. 모델 다운로드가 필요하므로 처음에는 인터넷을 사용합니다.
3. NVIDIA PC는 운영체제에서 GPU와 드라이버가 정상인지 확인합니다. Mac은 Apple Silicon인지 확인합니다. GPU 이름을 앱이 제대로 표시하는지 봅니다.
4. 처음부터 큰 모델을 여러 개 내려받지 말고, [7장](07-local-inference.md)의 Laya 체험이나 [9장](09-studio-training.md)의 0.8B 학습 중 하나로 시작합니다.

다운로드  [Unsloth Desktop](https://unsloth.ai/download)

근거: [3. Windows 설치](https://unsloth.ai/docs/get-started/install/windows-installation) · [4. Mac 설치](https://unsloth.ai/docs/get-started/install/mac) · [5. Linux 설치](https://unsloth.ai/docs/get-started/install/linux)

## 브라우저형 Studio를 직접 설치하는 경우

아래는 Desktop 설치 대신 선택하는 공식 Studio 설치 방식입니다. 원격의 설치 스크립트를 내려받아 실행합니다. 두 방식을 모두 설치할 필요는 없습니다.

**macOS 또는 Linux 터미널**

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

**Windows PowerShell**

```powershell
irm https://unsloth.ai/install.ps1 | iex
```

**설치 후 Studio 실행과 접속**

```text
unsloth studio -H 127.0.0.1 -p 8888
http://127.0.0.1:8888
```

두 번째 줄은 브라우저 주소창에 입력합니다. 첫 실행 때 계정 또는 비밀번호 안내가 나타나면 설정합니다. 위 명령은 내 PC에서 접속하는 실습을 기준으로 합니다. Desktop의 내부 포트가 다르면 앱 설정에 표시된 주소를 사용합니다.

## 코드 환경을 따로 구성할 때의 기준

Studio 설치는 학습 환경을 구성하는 쉬운 방법입니다. 별도의 Python 코드 환경은 사용 중인 터미널에서 같은 환경을 선택해야 합니다. Python 3.12를 기준으로 공식 운영체제별 Core 설치 안내를 따르세요. CUDA, ROCm, XPU, MLX 패키지를 하나의 명령으로 모든 PC에 설치할 수 있다고 가정하지 않습니다.

근거: [6. Studio 설치와 하드웨어 조건](https://unsloth.ai/docs/new/studio/install)

---

[전체 목차](../README.md) · [이전 장](05-pc-environments.md) · [다음 장](07-local-inference.md)
