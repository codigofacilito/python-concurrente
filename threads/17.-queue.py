import time
import queue
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def show_elements():
    while not queue.empty():
        item = queue.get()

        logging.info(f'El elemento es: {item}')

        queue.task_done()

        time.sleep(0.5)

if __name__ == '__main__':
    queue = queue.Queue() #FIFO

    for val in range(1, 20):
        queue.put(val)

    logging.info('La cola ya posee elementos!')

    for _ in range(4):
        thread = threading.Thread(target=show_elements)
        thread.start()
