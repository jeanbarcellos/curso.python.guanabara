# Crie um código em python que este se o site Pudim está acessível pelo computador usado.

import requests

try:
    url = 'http://www.pudims.com.br/'
    response = requests.get(url)

    print(f'\033[1;33mConsegui acessar o site do Pudim com sucesso.')

except Exception as erro:
    print(f'\033[1;31mO site Pudim não está acessível no momento.')
