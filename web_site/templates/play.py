import requests
api_url = "https://api.unminable.com/v4/account/5ddd86ec-17a7-4e64-8ff9-81b908fe542f?=balance"

response = requests.get(api_url)
response.json()
# print(response.json())
first_header = response.json()

print( first_header )