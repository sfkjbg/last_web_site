import self as self

from . import db
from flask_login import UserMixin, current_user
from sqlalchemy.sql import func
from flask import flash
import requests


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Api():
    def api():
        api_url = "https://api.unminable.com/v4/account/5ddd86ec-17a7-4e64-8ff9-81b908fe542f?=balance"
        r = requests.get(api_url)
        return r



def api(self):
    r = requests.get('https://api.unminable.com/v4/account/5ddd86ec-17a7-4e64-8ff9-81b908fe542f?=balance')
    api = r.json()
    return api