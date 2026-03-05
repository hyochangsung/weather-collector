import pytest
from src.parser import parse_weather

def test_parse_weather():
    sample_data = {
        "response": {
            "body": {
                "items": {
                    "item": [
                        {
                            "wf": "맑음",
                            "ta": "11",
                            "rnSt": 10
                        }
                    ]
                }
            }
        }
    }

    res = parse_weather(sample_data)

    assert isinstance(res, list)
    assert res[0]["wf"] == "맑음"
    assert res[0]["ta"] == "11"