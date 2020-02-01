from flask import Flask
import os
from ticker import tickerdata
from flask import jsonify


app = Flask(__name__)

env = os.environ.get('ENV', 'DEV')
conf = {
    'DEV': 'ticker.config.Develop',
    'PROD': 'ticker.config.Production',
    'TEST': 'ticker.config.Testing'
}[env]
app.config.from_object(conf)

@app.route('/')
def index():
    return "Hello world"


@app.route('/tickerdata')
def endpoint1():
    return jsonify(tickerdata.get_data())


