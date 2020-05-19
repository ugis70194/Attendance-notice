import requests
import json
import os 
import datetime

MONDAY_LECTUR = [("技術者倫理", os.environ["engineer_ethics"]) ,("空きコマ", os.environ["empty"]),("計算機アーキテクチャ", os.environ["architecture"]),("基礎制御工学", os.environ["basic_control_engineering"])]
TUESDAY_LECTUR = [("英語IV", os.environ["english"]) ,("情報理論", os.environ["information_theory"]),("電気磁気学", os.environ["electromagnetism"]),("情報通信ネットワーク", os.environ["network"])]
WEDNESDAY_LECTUR = [("保健体育", os.environ["P.E"]) ,("数学特講", os.environ["math"]),("電気回路", os.environ["electric_circuit"]),("空きコマ", os.environ["empty"])]
THURSDAY_LECTUR = [("応用物理", os.environ["applied_physics"]) ,("応用数学", os.environ["applied_math"]),("ソフトウェア工学", os.environ["software"]),("空きコマ", os.environ["empty"])]
FRIDAY_LECTUR = [("空きコマ", os.environ["empty"]) ,("ソフトウェア工学", os.environ["software"]),("電子回路", os.environ["electronic_circuit"]),("物理特講", os.environ["pysics"])]
LECTUR = [MONDAY_LECTUR, TUESDAY_LECTUR, WEDNESDAY_LECTUR, THURSDAY_LECTUR, FRIDAY_LECTUR]

def main():
    webhook = os.environ["webhook"]
    session = requests.session()
    header = { "Content-Type" : "application/json" }
    idx = -1
    today = datetime.datetime.now(datetime.timezone.utc)
    weekday = today.weekday()
    hour = today.hour
    minute = today.minute
    
    if hour == 23 and 40 <= minute <= 50 : 
        idx = 0
        weekday += 1
        weekday %= 7
    if hour == 1 and 20 <= minute <= 30 : idx = 1
    if hour == 3 and 0 <= minute <= 10 : idx = 2
    if hour == 5 and 20 <= minute <= 30 : idx = 3
    if hour == 7 and 0 <= minute <= 10 : idx = 4

    if idx == -1 : return
    if weekday == 5 or weekday == 6 :
        return

    lecture = LECTUR[weekday]
    if idx != 0 :
        idx -= 1
        if lecture[idx][0] != "空きコマ" :
            data = json.dumps({"content" : lecture[idx][0] + " 退席確認: " + lecture[idx][1]})
            response = session.post(webhook, headers=header, data=data)
        idx += 1
    if idx != 4 : 
        if lecture[idx][0] != "空きコマ" :
            data = json.dumps({"content" : lecture[idx][0] + " 出席確認: " + lecture[idx][1]})
            response = session.post(webhook, headers=header, data=data)

if __name__ == "__main__" :
    main()