import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATABASE_URL = 'postgres://dlavmtxtspfvyi:57d4109bdc70b283acdf1183fb967a0c717e2719bb9fa83aa900f79ccf293fbf@ec2-46-137-156-205.eu-west-1.compute.amazonaws.com:5432/deepag3mr5vvva'
    SQLALCHEMY_TRACK_MODIFICATIONS = False