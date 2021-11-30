import requests
import json


def FegToken():
    coin_url = 'https://api.coingecko.com/api/v3/simple/price?ids=feg-token&vs_currencies=USD'
    coin_r = requests.get(coin_url)
    coin_r = coin_r.text
    token_price = json.loads(coin_r)
    m = token_price['feg-token']
    feg_token = list(m.items())[0][1]
    print('FEG Token price')
    print(feg_token)
    return feg_token
# FegToken()
feg_balance = 108507182523.9313047
tot = feg_balance * FegToken()
print(tot)

# Marsh/ USDT - balance in kucoin
def marsh():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=unmarshal&vs_currencies=USD'
    url_r = requests.get(url)
    url_r = url_r.text
    py = json.loads(url_r)
    print(py)
marsh()

# RMRK/ USDT - balance in kucoin
def rmrk():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=rmrk&vs_currencies=USD'
    url_r = requests.get(url)
    url_r = url_r.text
    py_url_r = json.loads(url_r)
    print(py_url_r)
rmrk()




