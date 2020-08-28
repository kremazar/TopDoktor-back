from flask import Blueprint, jsonify, request, current_app
from app import app
from flask import render_template, flash, redirect
from app.models import User,Doktori,Ocjena
from flask import request,url_for
from werkzeug.urls import url_parse
from app import db
from flask_cors import CORS, cross_origin
import jwt
from datetime import datetime, timedelta

@cross_origin()


@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.get_json(force=True)
    user = User.authenticate(**data)

    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401
    token = jwt.encode({
        'id':user.id,
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({ 'token': token.decode('UTF-8') })

@app.route('/register', methods=['GET', 'POST'])
def register():
    email=request.get_json(force=True)['email']
    password=request.get_json(force=True)['password']
    user = User(email=email,password=password)
    db.session.add(user)
    db.session.commit()
    result={
        'email':email,
        'password':password,
    }
    return jsonify({'result':result})

@app.route('/ocjeni', methods=['GET', 'POST'])
def ocjeni():
    ocjena=request.get_json(force=True)['ocjena']
    komentar=request.get_json(force=True)['komentar']
    user_id=request.get_json()['user_id']
    doktor_id=request.get_json()['doktor_id']
    ocjena = Ocjena(ocjena=ocjena,komentar=komentar, user_id=user_id,doktor_id=doktor_id)
    db.session.add(ocjena)
    db.session.commit()
    result={
        'ocjena':ocjena,
        'komentar':komentar,
        'user_id':user_id,
        'doktor_id':doktor_id
    }
    return jsonify({'result':result})
    

@app.route('/dodajDoktora', methods=['GET', 'POST'])
def dodaj_doktora():
    ime=request.get_json(force=True)['ime']
    prezime=request.get_json(force=True)['prezime']
    specijalizacija=request.get_json(force=True)['specijalizacija']
    bolnica=request.get_json(force=True)['bolnica']
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

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    doktor = Doktori.query.filter_by(id=id).first()
    db.session.delete(doktor)
    db.session.commit()
    return "Obrisano"


@app.route('/doktori')
def doktori():
    doktor = Doktori.query.order_by(Doktori.prezime).all()
    return { "data": [
        {"id": doc.id,"ime": doc.ime,"prezime": doc.prezime,"specijalizacija": doc.specijalizacija,"bolnica": doc.bolnica}
        for doc in doktor
    ]}

@app.route('/ocjena')
def ocjena():
    ocjena = Ocjena.query.all()
    return { "data": [
        {"id": doc.id,"ocjena": doc.ocjena,"komentar": doc.komentar,"doktor_id": doc.doktor_id,"user_id": doc.user_id}
        for doc in ocjena
    ]}

@app.route('/doktor/<id>')
def doktor(id):
    doktor = Doktori.query.filter_by(id=id).first()
    return { "data": [
        {"id": doktor.id,"ime": doktor.ime,"prezime": doktor.prezime,"specijalizacija": doktor.specijalizacija,"bolnica": doktor.bolnica}
    ]}

@app.route('/najbolji')
def najbolji():
    sve = Doktori.query.join(Ocjena, Doktori.id==Ocjena.doktor_id).add_columns(Doktor.id,Doktor.ime,Doktor.prezime,Doktor.bolnica,Doktor.specijalizacija,Ocjena.ocjena).filter_by(Ocjena.ocjena)
    return { "data": [
        {"id": sve.id,"ime": sve.ime,"prezime": sve.prezime,"specijalizacija": sve.specijalizacija,"bolnica": sve.bolnica,"ocjena":sve.ocjena}
    ]}