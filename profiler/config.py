import os


POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")

CACHE_REDIS_HOST = os.getenv("CACHE_REDIS_HOST")
CACHE_REDIS_PORT = os.getenv("CACHE_REDIS_PORT")
CACHE_REDIS_USERNAME = os.getenv("CACHE_REDIS_USERNAME")
CACHE_REDIS_PASSWORD = os.getenv("CACHE_REDIS_PASSWORD")
CACHE_REDIS_DB = os.getenv("CACHE_REDIS_DB")


SECRET_KEY = os.getenv('SECRET_KEY')

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = SECRET_KEY

    # Redis Cache Config
    CACHE_TYPE = "SimpleCache"  # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT=60
    CACHE_REDIS_URL=f"redis://{CACHE_REDIS_HOST}:{CACHE_REDIS_PORT}/{CACHE_REDIS_DB}"
   
    

    #SQLALCHEMY Config
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
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Redis Cache Config
    CACHE_TYPE = "RedisCache"  # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT=1800
    CACHE_REDIS_URL=f"redis://{CACHE_REDIS_HOST}:{CACHE_REDIS_PORT}/{CACHE_REDIS_DB}"

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = False