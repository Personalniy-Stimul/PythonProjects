URL = 'https://api.pokemonbattle.ru/v2/'

TOKEN = 'ca389778e05f96a503b3cb965df76914'

HEADER = {
    'Content-Type' : 'application/json', 
    'trainer_token' : TOKEN
    }

BODY_CREATE = {
    "name": "Бульбазавр",
    "photo_id": 1
    }

BODY_NEW_NAME = {
    "pokemon_id": "122809",
    "name": "Ходэр",
    "photo_id": 1
    }

BODY_ADD_IN_POKEBALL = {
    "pokemon_id": "122809"
    }

import requests

response = requests.post(url = f'{URL}pokemons', headers = HEADER, json = BODY_CREATE)
print(response.text)

response = requests.put(url = f'{URL}pokemons', headers = HEADER, json = BODY_NEW_NAME)
print(response.text)

response = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = BODY_NEW_NAME)
print(response.text)

