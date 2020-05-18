import requests
import json
import os 
import datetime

MONDAY_LECTUR = [("技術者倫理", os.environ["engineer_ethics"]) ,("空きコマ", os.environ["empty"]),("計算機アーキテクチャ", os.environ["architecture"]),("基礎制御工学", os.environ["basic_control_engineering"])]
TUESDAY_LECTUR = [("英語IV", os.environ["empty"]) ,("情報理論", os.environ["information_theory"]),("電気磁気学", os.environ["electromagnetism"]),("情報通信ネットワーク", os.environ["network"])]
LECTUR = [MONDAY_LECTUR, TUESDAY_LECTUR]

def main():
    webhook = os.environ["webhook"]
    session = requests.session()
    header = { "Content-Type" : "application/json" }
    idx = -1
    today = datetime.datetime.now(datetime.timezone.utc)
    weekday = today.weekday()
    if weekday == 6 : weekday = 0
    hour = today.hour
    minute = today.minute
    
    if hour == 23 and 40 <= minute <= 50 : 
        idx = 0
        weekday += 1
    if hour == 1 and 20 <= minute <= 30 : idx = 1
    if hour == 3 and 0 <= minute <= 10 : idx = 2
    if hour == 5 and 20 <= minute <= 30 : idx = 3
    if hour == 7 and 0 <= minute <= 10 : idx = 4

    if idx == -1 : return

    lecture = LECTUR[weekday]
    if idx != 0 :
        idx -= 1
        print(lecture[idx])
        data = json.dumps({"content" : lecture[idx][0] + " 退席確認: " + lecture[idx][1]})
        response = session.post(webhook, headers=header, data=data)
        idx += 1
    if idx != 4 : 
        data = json.dumps({"content" : lecture[idx][0] + " 出席確認: " + lecture[idx][1]})
        response = session.post(webhook, headers=header, data=data)

if __name__ == "__main__" :
    main()