import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def nueva_tarea():
    current_thread = threading.current_thread()
    name = current_thread.getName()
    id = threading.get_ident()

    logging.info(f'El Thread actual es: {current_thread} y su nombre es: {name}')
    logging.info(f'El id actual es: {id}')

if __name__ == '__main__':
    thread1 = threading.Thread(target=nueva_tarea, name='thread-facilito')
    thread1.start()

    #logging.info(f'Los threads vivos son: {threading.enumerate()}')
    for thread in threading.enumerate():
        if thread == threading.main_thread():
            logging.info('Nos encontramos en el thread principal!')

        logging.info(thread)
