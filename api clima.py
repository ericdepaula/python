import requests
import json

clima = requests.get('http://apiadvisor.climatempo.com.br/api/v1/climate/rain/locale/3477?token=fc26e54adaef9f5f70eaa6db017318fd')
clima = clima.json()

print(clima)

# fc26e54adaef9f5f70eaa6db017318fd key
# 3823 id