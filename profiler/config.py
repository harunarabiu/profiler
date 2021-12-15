import os

SECRET_KEY = os.getenv('SECRET_KEY')

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = SECRET_KEY
    
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    


class DevelopmentConfig(BaseConfig):
    TESTING = False

    SQLALCHEMY_DATABASE_URI = f"sqlite://test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LiveConfig(BaseConfig):
    TESTING = False
    DEBUG = False
    
    SQLALCHEMY_DATABASE_URI = f"sqlite://test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = False