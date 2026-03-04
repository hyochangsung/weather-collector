import logging

# 1. fetcher에서 받아온 JSON 데이터를 인자로 받기
def parse_weather(data: dict):
    '''
    fetcher에서 반환된 값 정리
    '''
    if data is None:
        logging.error("파싱할 데이터가 없습니다.")
        return None

    # 2. JSON 데이터에서 필요한 값만 따로 변수에 저장하기
    items = data["response"]["body"]["items"]["item"]

    result = []

    for item in items:
        result.append({
            "wf": item["wf"],
            "ta": item["ta"],    
            "rnSt": item["rnSt"]
        })
    # 3. saver.py에서 가져갈 수 있게 반환하기

    return result
