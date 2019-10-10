import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Timer
def callback():
    logging.info('Hola, soy un callback que no ejecuta de forma inmediata')

if __name__ == '__main__':
    thread = threading.Timer(3, callback)
    thread.start()

    logging.info('Hola, soy el thread principal')
    logging.info('Estamos a la espera de la ejecución del callback')
