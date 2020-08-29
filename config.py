import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    """ SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/web' """
    SQLALCHEMY_TRACK_MODIFICATIONS = False