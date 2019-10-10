import time
import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

def is_even(number):
    time.sleep(1)
    return number % 2 == 0

def show_result(results):
    logging.info(f'El resultado es: {results}')

if __name__ == '__main__':
    with Pool(processes=2) as executor:
        numbers = [ number for number in range(1, 11)]

        for element in executor.imap_unordered(is_even, numbers): # yield
            logging.info(element)
