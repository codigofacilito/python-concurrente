import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def proceso_hijo():
    logging.info('Hola, desde el procesos hijo!')

    time.sleep(2)

    logging.info('Fin del proceso hijo!')

if __name__ == '__main__':
    process = multiprocessing.Process(target=proceso_hijo)
    process.start()

    time.sleep(5)

    if process.is_alive():
        process.terminate()
        logging.info('Proceso hijo finalizado antes de tiempo')

    logging.info('Fin del programa!')
