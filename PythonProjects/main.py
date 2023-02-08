import requests
import json
token = '29486d4b4e46c63e521b7de8c2e8ec33'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token},
json = {
    "name": "Kinders",
    "photo": 'https://www.freeiconspng.com/thumbs/pokemon-png/render-pokemon-png-1.png'
})
print(response.text)

pokemon_id = response.json()['id']
response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token},
json = {
    "pokemon_id": pokemon_id,
    "name": "Kinder",
    "photo": 'https://www.freeiconspng.com/thumbs/pokemon-png/render-pokemon-png-1.png'
})
print (response_change.text)

pokemon_id = response.json()['id']
response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type': 'application/json', 'trainer_token': token},
json = {
    "pokemon_id": pokemon_id
})
print(response.text)