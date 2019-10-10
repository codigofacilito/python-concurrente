import logging
import requests
import threading
from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def show_pokemon_name(response):
    if response.status_code == 200:
        response_json = response.json()
        name = response_json.get('forms')[0].get('name')

        logging.info(f'El nombre del pokemon es {name}')

def generate_request(url):
    future = Future()

    thread = threading.Thread(target=(
        lambda: future.set_result(requests.get(url))
    ))
    thread.start()

    return future

if __name__ == '__main__':
    future = generate_request('https://pokeapi.co/api/v2/pokemon/1/')
    future.add_done_callback(
        lambda future: show_pokemon_name(future.result())
    )

    while not future.done():
        logging.info('A la espera de un resultado')
    else:
        logging.info('Terminamos el programa!')
