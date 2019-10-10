import time
import logging
import threading

from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Futures = Abstracción de un resultado
# Javascript = Promesas

def callback_future(future):
    logging.info('Hola, soy un callback que se ejecuta hasta que el futuro posea un valor!')
    logging.info(f'El futuro es: {future.result()}')

if __name__ == '__main__':
    future = Future()
    future.add_done_callback(callback_future)
    future.add_done_callback(
        lambda future: logging.info('Hola, soy una lambda!')
    )

    logging.info('Comenzamos una tarea muy compleja!!!')

    time.sleep(2)

    logging.info('Terminamos la tarea compleja')

    logging.info('Vamos asignar un valor al futuro')

    future.set_result('CodigoFacilito')

    logging.info('El futuro ya posee un valor')
