import requests
import json
import time

roda = True

while(roda):
    def countdown(num_of_secs):
        while num_of_secs:
            m, s = divmod(num_of_secs, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            # print(min_sec_format)
            time.sleep(1)
            num_of_secs -= 1
            
    countdown(60)

    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacao = cotacao.json()
    cotacao_dol = cotacao['USDBRL']['bid']
    print('Cotação do Dólar:', cotacao_dol)

roda = countdown()