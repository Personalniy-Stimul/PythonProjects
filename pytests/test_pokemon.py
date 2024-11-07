import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'

TOKEN = 'ca389778e05f96a503b3cb965df76914'

HEADER = {
    'Content-Type' : 'application/json', 
    'trainer_token' : TOKEN
    }

def test_status_code():
    response = requests.get(url = f'{URL}trainers', headers = HEADER, params = {'trainer_id' : '8693'})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}trainers', headers = HEADER, params = {'trainer_id' : '8693'})
    assert response_get.json()["data"][0]['trainer_name'] == 'Незнайка'

