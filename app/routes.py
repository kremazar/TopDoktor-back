from flask import render_template,jsonify,json,request
from app import app
from flask import render_template, flash, redirect
from app.models import User,Doktori,Ocjena
from flask import request,url_for
from werkzeug.urls import url_parse
from app import db
from flask_cors import CORS, cross_origin


@cross_origin()


@app.route('/login', methods=['GET', 'POST'])
def login():
    email=request.get_json()['email']
    password=request.get_json()['password']
    user = User.query.filter_by(email=email).first()
    if user.password == password:
        result="OK"
    else:
        result = jsonify({"error": "invalid email and password"})
    return result

@app.route('/register', methods=['GET', 'POST'])
def register():
    username=request.get_json()['username']
    email=request.get_json()['email']
    password=request.get_json()['password']
    user = User(username=username, email=email,password=password)
    db.session.add(user)
    db.session.commit()
    result={
        'username':username,
        'email':email,
        'password':password,
    }
    return jsonify({'result':result})

@app.route('/ocjeni', methods=['GET', 'POST'])
def ocjeni():
    ocjena=request.get_json()['ocjena']
    user_id=request.get_json()['user_id']
    doktor_id=request.get_json()['doktor_id']
    ocjena = Ocjena(ocjena=ocjena, user_id=user_id,doktor_id=doktor_id)
    db.session.add(ocjena)
    db.session.commit()
    result={
        'ocjena':ocjena,
        'user_id':user_id,
        'doktor_id':doktor_id
    }
    return jsonify({'result':result})
    

@app.route('/dodajDoktora', methods=['GET', 'POST'])
def dodaj_doktora():
    ime=request.get_json()['ime']
    prezime=request.get_json()['prezime']
    specijalizacija=request.get_json()['specijalizacija']
    bolnica=request.get_json()['bolnica']
    doktor = Doktori(ime=ime, prezime=prezime,specijalizacija=specijalizacija,bolnica=bolnica)
    db.session.add(doktor)
    db.session.commit()
    result={
        'ime':ime,
        'prezime':prezime,
        'specijalizacija':specijalizacija,
        'bolnica':bolnica,
    }
    return jsonify({'result':result})


@app.route('/doktori')
def doktori():
    doktor = Doktori.query.all()
    return { "data": [
        {"id": doc.id,"ime": doc.ime,"prezime": doc.prezime,"specijalizacija": doc.specijalizacija,"bolnica": doc.bolnica}
        for doc in doktor
    ]}

@app.route('/doktor/<id>')
def doktor(id):
    doktor = Doktori.query.filter_by(id=id).first()
    return { "data": [
        {"id": doktor.id,"ime": doktor.ime,"prezime": doktor.prezime,"specijalizacija": doktor.specijalizacija,"bolnica": doktor.bolnica}
    ]}