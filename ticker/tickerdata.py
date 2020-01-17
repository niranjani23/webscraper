import requests
import json
import os
import pymongo

API_KEY = os.environ['WORLD_TRADING_DATA_API_KEY']


def get_data():
    resp = requests.get("https://api.worldtradingdata.com/api/v1/stock?symbol=LYFT&api_token=%s" % API_KEY)
    print(resp.text)
    data = json.loads(resp.text)
    print(data)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mystockdb"]
    mycol = mydb["tickerdata"]
    mydict = data
    print('*********')
    x = mycol.insert(mydict, manipulate=False)
    print(mydb.list_collection_names())
    return data

