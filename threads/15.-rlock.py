import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

BALANCE = 100

# Lock y RLock
lock = threading.RLock()

if __name__ == '__main__':

    lock.acquire() # Estado: Ocupado

    lock.acquire() # A la espera de que sea liberado

    BALANCE -= 10

    lock.release()

    lock.release()

    logging.info(f'Finalizamos el thread principal con el balance: {BALANCE}')
