import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

# Colas
def get_elements(queue):
    while not queue.empty():
        element = queue.get(block=True)
        logging.info(f'El elemento es: {element}')

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    queue = manager.Queue()

    for x in range(1, 21):
        queue.put(x)

    logging.info('La cola ya posee elementos!')

    process1 = multiprocessing.Process(target=get_elements, args=(queue, ))
    process2 = multiprocessing.Process(target=get_elements, args=(queue, ))
    process3 = multiprocessing.Process(target=get_elements, args=(queue, ))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

    logging.info('Fin de los procesos!')
