import time
import logging
import threading

#sleep(segundos)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)

if __name__ == '__main__':
    contador = 0

    while True:
        time.sleep(1)
        contador += 1
        logging.info(f'Tiempo transcurrido: {contador} segundos')
