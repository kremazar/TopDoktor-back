from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
        
class Ocjena(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ocjena = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    doktor_id = db.Column(db.Integer, db.ForeignKey('doktori.id'))

class Doktori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(120))
    prezime = db.Column(db.String(120))
    specijalizacija = db.Column(db.String(120))
    bolnica = db.Column(db.String(120))
    

 
  