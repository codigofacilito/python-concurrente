import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

BALANCE = 0

lock = threading.Lock()

def depositos():
    global BALANCE

    for _ in range(0, 1000000):
        try:
            lock.acquire()
            BALANCE += 1
        finally:
            lock.release()

def retiros():
    global BALANCE

    for _ in range(0, 1000000):
        with lock:
            BALANCE -= 1 # Sección critica

if __name__ == '__main__':
    thread1 = threading.Thread(target=depositos)
    thread2 = threading.Thread(target=retiros)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    logging.info(f'El valor final del balance es: {BALANCE}')
