import os

class Config():
    HOST = 'http://localhost:5000'
    SECRET_KEY = 'supersecret'
    JSONIFY_MIMETYPE = 'application/json'


class Develop(Config):
    DEBUG = True
    HOST = os.environ.get('HOST', Config.HOST)
    SECRET_KEY = os.environ.get('SECRET_KEY', Config.SECRET_KEY)
    JSONIFY_PRETTYPRINT_REGULAR = True



class Testing(Develop):
    TESTING = True #to block features if desired

class Production(Develop):
    PRODUCTION = True
    DEBUG = False
    JSONIFY_PRETTYPRINT_REGULAR = False

