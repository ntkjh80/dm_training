# 05. 내 PC에 맞는 경로 선택

| PC 환경 | 처음 할 일 | 내 데이터 학습 경로 |
| --- | --- | --- |
| Windows 또는 Linux와 NVIDIA GPU | Desktop 설치 후 작은 모델로 점검 | Studio 또는 CUDA 코드 실습 |
| Apple Silicon Mac | Desktop과 MLX 환경 확인 | 최신 MLX Decision 학습 경로 |
| Intel Mac | Laya 로컬 API 체험 | Colab GPU 학습부터 권장 |
| GPU 없는 Windows 또는 Linux | CPU로 Laya 실행 | Colab GPU 학습부터 권장 |
| AMD GPU | 공식 AMD 설치 절차 확인 | 지원 GPU와 모델 조합을 소량 검증 |
| Intel Arc 등 지원 Intel GPU | 공식 XPU 설치 절차 확인 | 지원 GPU와 모델 조합을 소량 검증 |

AMD와 Intel에도 Unsloth 설치 경로가 있습니다. 다만 일반 모델 학습 지원이 모든 Decision 모델의 양자화와 저장 조합까지 보장하지는 않습니다. 동봉 Python 학습 코드는 NVIDIA와 Apple Silicon을 대상으로 하며, AMD와 Intel은 설치기의 GPU 인식과 Studio의 소량 학습으로 확인합니다.

근거: [3. Windows 설치](https://unsloth.ai/docs/get-started/install/windows-installation) · [4. Mac 설치](https://unsloth.ai/docs/get-started/install/mac) · [5. Linux 설치](https://unsloth.ai/docs/get-started/install/linux) · [6. Studio 설치와 하드웨어 조건](https://unsloth.ai/docs/new/studio/install) · [10. Apple Silicon Decision 학습 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/decision_mlx.py) · [14. AMD 설치](https://unsloth.ai/docs/get-started/install/amd) · [15. Intel GPU 설치](https://unsloth.ai/docs/get-started/install/intel)

## 메모리를 확인할 때

Windows에서는 작업 관리자 → 성능 → GPU에서 전용 GPU 메모리를 확인합니다. 시스템 RAM과 VRAM은 다른 자원입니다. Mac에서는 이 Mac에 관하여에서 칩과 메모리를 확인하며, Apple Silicon의 통합 메모리는 운영체제와 앱도 함께 사용합니다. Linux의 NVIDIA 장치는 nvidia-smi로 확인할 수 있습니다.

수업 준비용 권장 여유값: 시스템 메모리 16GB 이상, 디스크 20GB 이상을 먼저 확보하고 0.8B부터 시도합니다. 4B나 16비트 병합본까지 보관하면 30GB 이상 여유가 필요할 수 있습니다. 이 숫자는 교육용 계획값이며 공식 최소 요구사항이나 실행 보장이 아닙니다.

NVIDIA VRAM 4GB 전후라면 0.8B도 길이와 batch를 낮춰 점검해야 합니다. 8GB 이상이면 작은 모델 선택 폭이 넓어집니다. Mac 8GB에서는 우선 Laya 실행을 체험하고, 학습은 작은 모델 또는 Colab을 고려합니다. 16GB나 24GB에서도 다른 앱 사용량에 따라 실패할 수 있습니다.

## Mac 지원을 정확히 구분하기

공식 구현에는 MLX용 FastDecisionModel과 DecisionTrainer가 존재합니다. 따라서 Apple Silicon에서 학습 자체가 불가능하다고 안내하면 틀립니다. 반대로 CUDA 코드의 GPU 설정을 그대로 Mac에 적용해서도 안 됩니다. 최신 앱과 관련 패키지가 필요하며, 이 교재는 각 독자의 기기에서 실제 학습 성공을 보장하지 않습니다.

근거: [10. Apple Silicon Decision 학습 구현](https://github.com/unslothai/unsloth/blob/main/unsloth/models/decision_mlx.py)

---

[전체 목차](../README.md) · [이전 장](04-source-benchmarks.md) · [다음 장](06-installation.md)
