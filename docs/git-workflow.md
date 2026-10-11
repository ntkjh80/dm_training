# Git으로 교재와 코드를 관리하기

[전체 목차](../README.md)

이 저장소는 교재, 강의 대본, 실습 코드, 교육용 가상 데이터를 함께 관리합니다. 설명을 수정하면 관련 코드와 같은 커밋에 기록할 수 있습니다.

## 1. 변경 상태와 이력 보기

터미널에서 `DM_training` 폴더를 열고 실행합니다.

```bash
git status
git log --oneline
```

현재 작업 브랜치는 `main`입니다. `git status`는 수정된 파일과 커밋할 파일을, `git log`는 저장한 변경 이력을 보여 줍니다.

## 2. 교재를 수정하고 커밋하기

예를 들어 PC 안내를 수정한 경우 다음처럼 해당 파일을 확인하고 저장합니다.

```bash
git diff -- docs/05-pc-environments.md
git add docs/05-pc-environments.md
git diff --cached
git commit -m "docs: PC별 학습 안내 보완"
```

`git diff --cached`에서 실제 커밋될 내용을 확인합니다. 데이터 형식이나 예제를 수정했다면 먼저 검사합니다.

```bash
python practice/train_decision.py --check-data
```

Markdown 표·코드 블록·문서 링크는 편집기의 미리보기에서도 확인하세요. 교재와 코드의 경로, 파일 이름, 옵션이 서로 맞아야 합니다.

## 3. Git에 저장하는 파일과 제외하는 파일

| 저장하는 파일 | 기본적으로 제외하는 파일 |
| --- | --- |
| Markdown 교재와 강의 대본 | 모델 가중치와 다운로드 캐시 |
| Python 실습 코드 | `outputs/`, `checkpoints/`, `models/` |
| 교육용 가상 JSONL 데이터 | `private-data/`의 개인 데이터 |
| 실제 키가 없는 API 요청 예제 | `.env`, `.env.*`의 로컬 설정 |
| `.gitignore`, `.gitattributes` | 가상환경과 Python 캐시 |

`.gitignore`는 목록에 맞는 경로를 제외합니다. 파일 내용에서 비밀 정보를 찾아 지워 주는 기능은 아닙니다. 실제 API 키는 코드와 Markdown에 붙여 넣지 말고 환경 변수로 설정합니다.

`metrics.json`과 `environment.txt`는 실행 결과 폴더에서 관리합니다. 수업에 공유할 실제 결과는 필요한 항목을 검토한 뒤 별도 Markdown 기록으로 옮길 수 있습니다. 민감한 경로나 원문이 함께 들어 있지 않은지 확인합니다.

## 4. 나중에 GitHub와 연결하기

Git은 로컬 변경 이력을 관리하고 GitHub는 원격 저장소를 제공합니다. 이 로컬 저장소를 GitHub에서 공유하려면 계정에서 빈 저장소를 만든 뒤 생성 화면의 URL을 사용합니다. 기존 로컬 이력이 있으므로 원격에서 README를 새로 생성하지 않는 편이 간단합니다.

다음 예시의 계정과 저장소 이름을 실제 URL로 바꿉니다.

```bash
git remote add origin https://github.com/YOUR_ACCOUNT/DM_training.git
git remote -v
git push -u origin main
```

`origin`이 이미 있다면 `git remote -v`로 먼저 확인합니다. 원격 연결과 업로드는 위 명령을 실행할 때 이루어집니다. 로그인 방식은 자신의 GitHub 계정 설정에 따릅니다.

## 5. 재현 가능한 수업 기록

교재 변경 이력과 모델 학습 결과는 함께 추적하면 유용합니다. 학습 시 다음 정보를 기록합니다.

- 교재 커밋: `git rev-parse HEAD`.
- 기반 모델과 실제 리비전.
- 질문 정의와 데이터 버전·해시.
- GPU, Python, Unsloth 및 관련 패키지 버전.
- 학습 설정, 보정 방식, 최종 시험 결과.
- 실제 실행 시간과 실패 사례.

커밋은 코드와 자료의 버전을 식별합니다. 별도 모델 파일이나 실행 환경까지 자동 보관하지는 않습니다.
