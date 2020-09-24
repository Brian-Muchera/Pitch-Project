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





