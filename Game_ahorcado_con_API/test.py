import requests
from random import choice


# Realiza una solicitud GET a la API
response = requests.get('https://clientes.api.greenborn.com.ar/public-random-word')
data = response.json()
word = data
print (word)