# webscraper
This project is a web crawler that looks for AAPL ticker symbol using the python library: https://api.worldtradingdata.com/api/v1/stock?symbol=AAPL and currently returns the json blurb of the response data.



"source venv/bin/activate" activated virtual environment while developing this project. 

"pip3 freeze" was used to freeze the following requirements:
certifi==2019.6.16
chardet==3.0.4
Click==7.0
configobj==5.0.6
Flask==1.1.1
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
personal==0.1.1
protobuf==3.9.1
pycrypto==2.6.1
PyJWT==1.7.1
pytz==2019.3
repo==0.1.0
requests==2.22.0
six==1.12.0
twilio==6.33.1
urllib3==1.25.3
Werkzeug==0.15.5

Python 3.7 has been used for this project.

"export WORLD_TRADING_DATA_API_KEY=xxxx" was set within the virtualenv

"python3 server.py" starts the python flask server locally

Now run "python3 tickerdata.py" and it should return the current value of AAPL stock in json.

Install Heroku and configure it to connect to github account. 

Add Procfile: web: python3 server.py

Now this file will be picked up by HEroku and it'll start running the server. 
It generated the following URL for consumption: http://py-webscraper.herokuapp.com/tickerdata
