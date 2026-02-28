# weather-collector
📌 공개 날씨 API를 활용해 데이터를 수집·저장·분석하는 CLI 기반 데이터 파이프라인 프로젝트입니다. 이후 DB, Docker, Airflow로 확장 가능한 구조로 설계되었습니다.

## 프로젝트 구조
```
weather-collector/
│
├── src/
│   ├── __init__.py   # 이 폴더를 파이썬 패키지로 인식하도록 설정
│   ├── fetcher.py    # 날씨 API 데이터 수집 모듈
│   ├── parser.py     # 수집한 데이터 파싱 처리 모듈
│   └── saver.py      # 데이터 저장 모듈
│
├── data/             # 수집된 데이터 저장 폴더 (GitHub 업로드 제외)
├── main.py           # 프로그램 실행 진입점
├── requirements.txt  # 프로젝트 의존성 라이브러리 목록
└── .gitignore        # Git 추적 제외 파일 설정
```
