from base import *
import json
import os 

data = json.dumps({"content" : "計算機アーキテクチャ退席確認: " + os.environ["architecture_leaving"]})
response = session.post(webhook, headers=header, data=data)