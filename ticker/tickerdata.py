import requests
import json
import os

API_KEY = os.environ['WORLD_TRADING_DATA_API_KEY']


def get_data():
    resp = requests.get("https://api.worldtradingdata.com/api/v1/stock?symbol=AAPL&api_token=%s" % API_KEY)
    print(resp.text)
    data = json.loads(resp.text)
    #print(data)
    return data
