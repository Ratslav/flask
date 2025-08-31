import os

from dotenv import load_dotenv

load_dotenv()
MY_SECRET_KEY = os.getenv('MY_SECRET_KEY')
DATABASE_URI = os.getenv('DATABASE_URI')


class Config(object):
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SECRET_KEY = MY_SECRET_KEY
