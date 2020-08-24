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




@app.route('/register', methods=['GET', 'POST'])
def register():
    email=request.get_json()['email']
    password=request.get_json()['password']
    user = User(email=email,password=password)
    db.session.add(user)
    db.session.commit()
    result={
        'email':email,
        'password':password,
    }
    return jsonify({'result':result})

