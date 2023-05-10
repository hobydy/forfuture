from binance import Client
import requests
from bs4 import BeautifulSoup

api_key = '1RrTe8IPPSZzgebyxAAgNApqjFWrsotdGGpl0Ah5OlNRwyFqVEL7rQ5QrITE1ADD'
secret_key = '8CsJdbMIBlTr3dHDpENf5JbsycdJbX9pILMoUm5NYKSqTZ4PI3i7Kb7ZxO9zW8Qg'

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
requsd = requests.get(urlusd)
soup = BeautifulSoup(requsd.text, 'html.parser')
mdlltcget = soup.find('div', class_="YMlKec fxKbKc")
if mdlltcget is not None:
    mdlltc = float(mdlltcget.text)
else:
    print("Unable to find the element for MDL-LTC")

# Достаем цену 1 лея в BTC
urlbtc = "https://www.google.com/finance/quote/MDL-BTC?sa=X&ved=2ahUKEwjwmOeRib7-AhXy7LsIHQ0TCQEQ-fUHegQIBhAf"
reqbtc = requests.get(urlbtc)
soup = BeautifulSoup(reqbtc.text, "html.parser")
mdlbtcget = soup.find('div', class_='YMlKec fxKbKc')
if mdlbtcget is not None:
    mdlbtcget = float(mdlltcget.text)
else:
    print("Unable to find the element for MDL-BTC")


# Достаем цену 1 лея в ETH
urleth = 'https://www.google.com/finance/quote/MDL-ETH?sa=X&ved=2ahUKEwiL_faTjL7-AhUdgf0HHb54BksQ-fUHegQIDhAf'
reqeth = requests.get(urleth)
soup = BeautifulSoup(reqeth.text, "html.parser")
mdlethget = soup.find('div', class_='YMlKec fxKbKc')
if mdlethget is not None:
    mdlethget = float(mdlltcget.text)
else:
    print("Unable to find the element for MDL-BTC")

