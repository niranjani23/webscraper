import requests
import json
import os
import pymongo
#from ticker import app #TODO: fix import in order to use app.config

API_KEY = os.environ['WORLD_TRADING_DATA_API_KEY']


def get_data():
    resp = requests.get("https://api.worldtradingdata.com/api/v1/stock?symbol=LYFT&api_token=%s" % API_KEY)
    print(resp.text)
    data = json.loads(resp.text)
    print(data)
    myclient = pymongo.MongoClient(os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/'), retryWrites=False)
    mydb = myclient["mystockdb"]
    mycol = mydb["tickerdata"]
    mydict = data
    print('*********')
    x = mycol.insert(mydict, manipulate=False)
    print(mydb.list_collection_names())
    return data

