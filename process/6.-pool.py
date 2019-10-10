import time
import logging
# from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

def is_even(number):
    time.sleep(5)
    return number % 2 == 0

if __name__ == '__main__':
    with Pool(processes=2) as executor:

        apply_result = executor.apply_async(is_even, args=(10, ))

        logging.info(apply_result)

        logging.info('Vamos a esperar hasta que apply_result posea un valor')

        apply_result.wait(timeout=2)

        logging.info('Apply_result ha finalizado')

        logging.info(f'El resultado es: {apply_result.get(timeout=1)}')

        logging.info(f'Fin del programa')
