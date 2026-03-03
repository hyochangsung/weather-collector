import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")

REGION_CODE = {
    "서울": "11B10101",
    "인천": "11B20201",
    # 필요한 도시 추가
}

def fetch_weather(city: str):
    '''
    도시의 이름을 입력 받아서 날씨 데이터를 API로부터 가져오는 함수
    '''
    reg_id = REGION_CODE.get(city)

    if reg_id is None:
        logging.error(f"지원하지 않는 도시입니다: {city}")
        return None

    params = {
        "pageNo": 1,
        "numOfRows": 10,
        "dataType": "JSON",
        "regId": reg_id,
        "authKey": api_key
    }

    # API 호출하기
    response = requests.get(base_url, params=params)
    
    #성공시 데이터 반환
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"API 호출 실패: {response.status_code}")
        return None

if __name__ == "__main__":
    result = fetch_weather("서울")
    print(result)