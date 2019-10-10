import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(process)s %(processName)s %(message)s')

def nuevo_proceso(mensaje):
    logging.info('Hola, soy un nuevo proceso')

    time.sleep(3)

    logging.info(mensaje)

    logging.info('Fin del proceso')

if __name__ == '__main__':
    # args o kwargs
    process = multiprocessing.Process(target=nuevo_proceso, name='proceso-hijo',
                                        kwargs={'mensaje': 'Nuevo mensaje, desde un argumento!'})
    process.start()

    process.join()

    logging.info('Hola, desde el proceso padre')
