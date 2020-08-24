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