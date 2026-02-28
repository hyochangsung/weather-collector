# weather-collector
📌 공개 날씨 API를 활용해 데이터를 수집·저장·분석하는 CLI 기반 데이터 파이프라인 프로젝트입니다. 이후 DB, Docker, Airflow로 확장 가능한 구조로 설계되었습니다.

## 프로젝트 구조
weather-collector/
│
├── src/
│   ├── __init__.py   # 이 폴더가 파이썬 패키지임을 알려줌
│   ├── fetcher.py    # API 호출 담당
│   ├── parser.py     # 데이터 파싱 담당
│   └── saver.py      # 데이터 저장 담당
│
├── data/             # 수집한 데이터 저장 (GitHub에 올리지 않음)
├── main.py           # 실행 진입점
├── requirements.txt  # 설치한 라이브러리 목록
└── .gitignore        # Git에서 제외할 파일 목록
