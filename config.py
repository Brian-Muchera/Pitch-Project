import os

from dotenv import load_dotenv as ld

ld()


class Config:
    debug = True
    SECRET_KEY = '0443'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://muchera-brian:brian@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://muchera-brian:brian@localhost/pitch'
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://muchera-brian:brian@localhost/pitch'
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}



