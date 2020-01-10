import requests
import json
import os
import pymongo

API_KEY = os.environ['WORLD_TRADING_DATA_API_KEY']


def get_data():
    resp = requests.get("https://api.worldtradingdata.com/api/v1/stock?symbol=AAPL&api_token=%s" % API_KEY)
    print(resp.text)
    data = json.loads(resp.text)
    print(data)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mystockdb"]
    mycol = mydb["tickerdata"]
    mydict = data
    mydict2 = {
      "data": [
        {
          "52_week_high": "310.43",
          "52_week_low": "149.22",
          "change_pct": "2.12",
          "close_yesterday": "303.19",
          "currency": "USD",
          "day_change": "6.44",
          "day_high": "310.43",
          "day_low": "306.20",
          "eps": "11.89",
          "gmt_offset": "-18000",
          "last_trade_time": "2020-01-09 16:00:01",
          "market_cap": "1372775645184",
          "name": "Apple Inc.",
          "pe": "26.04",
          "price": "309.63",
          "price_open": "307.24",
          "shares": "4384030208",
          "stock_exchange_long": "NASDAQ Stock Exchange",
          "stock_exchange_short": "NASDAQ",
          "symbol": "AAPL",
          "timezone": "EST",
          "timezone_name": "America/New_York",
          "volume": "39450557",
          "volume_avg": "31645057"
        }
      ],
      "symbols_requested": 1,
      "symbols_returned": 1
    }
    print('*********')
    x = mycol.insert_one(mydict)
    #x = mycol.insert(mydict)
    print(mydb.list_collection_names())
    return data

