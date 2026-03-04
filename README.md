# weather-collector

📌 기상청 API를 활용해 날씨 데이터를 수집·저장·분석하는 CLI 기반 데이터 파이프라인 프로젝트입니다.  
이후 DB, Docker, Airflow로 확장 가능한 구조로 설계되었습니다.

---

## 프로젝트 구조

```
weather-collector/
│
├── src/
│   ├── __init__.py   # 이 폴더를 파이썬 패키지로 인식하도록 설정
│   ├── fetcher.py    # 날씨 API 데이터 수집 모듈 ✅
│   ├── parser.py     # 수집한 데이터 파싱 처리 모듈 ✅
│   └── saver.py      # 데이터 저장 모듈
│
├── data/             # 수집된 데이터 저장 폴더 (GitHub 업로드 제외)
├── .env              # API 키 등 환경변수 저장 (GitHub 업로드 제외)
├── main.py           # 프로그램 실행 진입점
├── requirements.txt  # 프로젝트 의존성 라이브러리 목록
└── .gitignore        # Git 추적 제외 파일 설정
```

---

## 사용 기술

- **Python 3.x**
- **requests** - 기상청 API 호출
- **python-dotenv** - 환경변수 관리

---

## 데이터 소스

- **기상청 API허브** - 육상예보조회 API
- API 주소: `https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstMsgService/getLandFcst`
- 제공 데이터:

| 변수명 | 의미 |
|--------|------|
| ta | 예상기온(°C) |
| rnSt | 강수확률(%) |
| wf | 날씨 |
| wfCd | 날씨코드(하늘상태) |
| wd1 | 풍향 |
| rnYn | 강수형태 |

---

## 환경 설정

### 1. 가상환경 생성 및 활성화

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 환경변수 설정

프로젝트 루트에 `.env` 파일 생성 후 아래 내용 작성:

```
BASE_URL=https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstMsgService/getLandFcst
API_KEY=발급받은_API_키
```

> 기상청 API 키는 https://apihub.kma.go.kr 에서 발급받을 수 있습니다.

---

## 지원 도시

| 도시 | 지역코드 |
|------|------|
| 서울 | 11B10101 |
| 인천 | 11B20201 |

> 추후 도시 추가 예정

---

## 진행 현황

- [x] 프로젝트 구조 설계 (모듈화)
- [x] 기상청 API 키 발급
- [x] 환경변수(.env) 설정
- [x] fetcher.py 구현 - 기상청 API 데이터 수집
- [x] parser.py 구현 - API 응답 데이터 파싱
- [ ] parser.py 테스트 코드 작성 (pytest)
- [ ] saver.py 구현
- [ ] main.py 연결
- [ ] DB 연동 (예정)
- [ ] Docker 컨테이너화 (예정)
- [ ] Airflow 파이프라인 (예정)
