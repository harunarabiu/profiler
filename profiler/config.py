import os

SECRET_KEY = os.getenv('SECRET_KEY')

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = SECRET_KEY
    

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///profile.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    


class DevelopmentConfig(BaseConfig):
    TESTING = False
    
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///profile.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LiveConfig(BaseConfig):
    TESTING = False
    DEBUG = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///profiler.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = False