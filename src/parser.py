import logging

# 1. fetcher에서 받아온 JSON 데이터를 인자로 받기
def parse_weather(data: dict):
    '''
    기상청 API 응답 데이터에서 날씨 정보를 추출하여 반환
    '''
    if data is None:
        logging.error("파싱할 데이터가 없습니다.")
        return None

    # 기상청 API 응답 구조상 item이 리스트로 감싸져 있음
    items = data["response"]["body"]["items"]["item"]

    result = []

    for item in items:
        result.append({
            "wf": item["wf"],
            "ta": item["ta"],    
            "rnSt": item["rnSt"]
        })

    return result