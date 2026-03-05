from src.fetcher import fetch_weather
from src.parser import parse_weather
from src.saver import save_weather

if __name__ == "__main__":
    
    city = input("날씨 정보를 원하는 도시를 작성하시오 : ")

    data = fetch_weather(city)
    if data is None:
        print("데이터 수집 실패")
        exit()

    parsed_data = parse_weather(data)
    if parsed_data is None:
        print("데이터 파싱 실패")
        exit()

   
    save_weather(parsed_data)