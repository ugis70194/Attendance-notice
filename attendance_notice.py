import requests
import json
import os 
import datetime

MONDAY_LECTUR = [("技術者倫理", os.environ["engineer_ethics"]) ,("空きコマ", os.environ["empty"]),("計算機アーキテクチャ", os.environ["architecture"]),("基礎制御工学", os.environ["basic_control_engineering"])]
LECTUR = [MONDAY_LECTUR]

def main():
    webhook = os.environ["webhook"]
    session = requests.session()
    header = { "Content-Type" : "application/json" }
    idx = -1
    weekday = datetime.date.today().weekday()
    if weekday == 6 : weekday = 0
    hour = datetime.datetime.today().hour
    minute = datetime.datetime.today().minute
    
    if hour == 23 : idx = 0
    if hour == 1 and 20 <= minute <= 30 : idx = 1
    if hour == 3 and 0 <= minute <= 10 : idx = 2
    if hour == 5 and 20 <= 30 : idx = 3
    if hour == 7 : idx = 4

    if idx == -1 : return

    lecture = LECTUR[weekday]
    if idx != 0 :
        data = json.dumps({"content" : lecture[idx][0] + " 退席確認: " + lecture[idx][1]})
        response = session.post(webhook, headers=header, data=data)
        idx += 1
    if idx != 5 : 
        data = json.dumps({"content" : lecture[idx][0] + " 出席確認: " + lecture[idx][1]})
        response = session.post(webhook, headers=header, data=data)

if __name__ == "__main__" :
    main()