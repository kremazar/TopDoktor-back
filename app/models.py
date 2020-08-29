from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    user_id = db.relationship('Ocjena', backref='user', lazy='joined')
    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password, method='sha256')
    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        
        if not email or not password:
            return None

        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def to_dict(self):
        return dict(id=self.id, email=self.email)
        
class Ocjena(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ocjena = db.Column(db.Float, asdecimal=False)
    komentar = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    doktor_id = db.Column(db.Integer, db.ForeignKey('doktori.id'))

class Doktori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(120))
    prezime = db.Column(db.String(120))
    specijalizacija = db.Column(db.String(120))
    bolnica = db.Column(db.String(120))
    doktor_id = db.relationship('Ocjena', backref='doktori', lazy='joined')

class Clanak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naslov = db.Column(db.String(120))
    opis = db.Column(db.String(1000))
    link = db.Column(db.String(120))
    

 
  