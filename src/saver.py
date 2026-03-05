# 1. 라이브러리 불러오기
import logging
import csv

def save_weather(datas: list):
    '''
    파싱된 날씨 데이터를 CSV 파일로 저장
    '''
    if datas is None:
        logging.error("넘어온 데이터가 없습니다")
        return None

    with open("data/weather.csv", "w", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["wf", "ta", "rnSt"])
        for data in datas:
            writer.writerow([data["wf"], data["ta"], data["rnSt"]])