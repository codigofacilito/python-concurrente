import time
import logging
import threading

from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

def math_operation(number1, number2):
    time.sleep(1)

    result = number1 + number2
    logging.info(f'Resultado de {number1} + {number2} = {result}')

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=3, thread_name_prefix='facilitos')

    executor.submit(math_operation, 10, 20)
    executor.submit(math_operation, 40, 50)

    executor.submit(math_operation, 100, 200)
    executor.submit(math_operation, 60, 70)
