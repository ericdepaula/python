import requests
import json

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacao = cotacao.json()
cotacao_dol = cotacao['USDBRL']['bid']
print("Cotação do Dólar:", cotacao_dol)

cotacao2 = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacao2 = cotacao2.json()
cotacao_eur = cotacao2['EURBRL']['bid']
print("Cotação do Euro:", cotacao_eur)
