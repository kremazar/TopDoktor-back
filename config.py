import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATABASE_URL = 'mysql+pymysql://root:''@localhost/web'
    SQLALCHEMY_TRACK_MODIFICATIONS = False