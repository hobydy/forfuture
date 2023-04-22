from binance import Client
import requests
from bs4 import BeautifulSoup

api_key = 'Your api key'
secret_key = 'Your secret key'

client = Client(api_key, secret_key)

# Достаем информацию о цене валюты через api binance
BTCUSDT = client.get_symbol_ticker(symbol="BTCUSDT")
LTCUSDT = client.get_symbol_ticker(symbol="LTCUSDT")
ETHUSDT = client.get_symbol_ticker(symbol="ETHUSDT")
# Присваем переменым полученые значения
btc_price = float(BTCUSDT['price'])
ltc_price = float(LTCUSDT['price'])
eth_price = float(ETHUSDT['price'])

# Достаем цену 1 лея в долларах
urlusd = 'https://www.google.com/finance/quote/MDL-LTC?sa=X&ved=2ahUKEwjI-IGfu73-AhVKxAIHHSidC_0Q-fUHegQIBhAf'
r = requests.get(urlusd)
soup = BeautifulSoup(r.text, 'html.parser')
mdlltcget = soup.find('div', class_="YMlKec fxKbKc").text
mdlltc = float(mdlltcget)

# Достаем цену 1 лея в BTC
urlbtc = "https://www.google.com/finance/quote/MDL-BTC?sa=X&ved=2ahUKEwjwmOeRib7-AhXy7LsIHQ0TCQEQ-fUHegQIBhAf"
r = requests.get(urlbtc)
soup = BeautifulSoup(r.text, "html.parser")
mdlbtcget = soup.find('div', class_='YMlKec fxKbKc').text
mdlbtc = float(mdlbtcget)

# Достаем цену 1 лея в ETH
urleth = 'https://www.google.com/finance/quote/MDL-ETH?sa=X&ved=2ahUKEwiL_faTjL7-AhUdgf0HHb54BksQ-fUHegQIDhAf'
r = requests.get(urleth)
soup = BeautifulSoup(r.text, "html.parser")
mdlethget = soup.find('div', class_='YMlKec fxKbKc').text
mdleth = float(mdlethget)
