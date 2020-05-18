import requests
import json
import os 

webhook = os.environ["webhook"]
session = requests.session()
header = { "Content-Type" : "application/json" }