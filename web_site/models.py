# import self as self
import json
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


# "Gets current balance of sol" -- Header
def Funcs():
    funcs = "Current mined balance of SOL "
    return funcs
# gets current balance on unminable sol account
def Api():
    api_url = "https://api.unminable.com/v4/account/5ddd86ec-17a7-4e64-8ff9-81b908fe542f?=balance"
    r = requests.get(api_url)
    r = r.text
    api = json.loads(r)
    m = api['data']
    fv = list(m.items())[0][1]
    api = fv
    return api
# gets the coin price of SOL @ coingecko
def Coin_Price():
    coin_url = 'https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=USD'
    coin_r = requests.get(coin_url)
    coin_r = coin_r.text
    coin_dict = json.loads(coin_r)
    m = coin_dict['solana']
    coin_price = list(m.items())[0][1]
    return coin_price
# get the total $value of sol : coin_price * api
def Total_Balance():
    coin_price = float(Coin_Price())
    api = float(Api())
    tots = api * coin_price
    return tots
#



#       {"success":true,"msg":"Ok","data":
#       {"balance":"0.00855695","balance_payable":"0.00855695","precision":"8",
#                                    "payment_threshold":"0.15","mining_fee":"1","auto":true,"enabled":true,
#                                    "uuid":"5ddd86ec-17a7-4e64-8ff9-81b908fe542f","coin":"SOL","network":"SOL"}}

## Working api
# def Api():
#     api_url = "https://api.unminable.com/v4/account/5ddd86ec-17a7-4e64-8ff9-81b908fe542f?=balance"
#     r = requests.get(api_url)
#     api = r.json()
#     return api

# def Api():
#     api_url = "https://api.unminable.com/v4/account/5ddd86ec-17a7-4e64-8ff9-81b908fe542f?=balance"
#     r = requests.get(api_url)
#     api = r.text
#     # for i in api['data']:
#     #     print(i)
#     # j = api['data']
#     # api = json.loads()
#     # # json.loads(json_string)
#     # api = j
#     return api