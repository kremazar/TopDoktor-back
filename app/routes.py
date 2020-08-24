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
    data = request.get_json()
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

