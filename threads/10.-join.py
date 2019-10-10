import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def conexion_base_datos():
    logging.info('Comenzamos la conexión a la base de datos')
    time.sleep(2)

def consulta_servidor_web():
    logging.info('Comenzamos la consulta al servidor')
    time.sleep(2.5)

if __name__ == '__main__':
    thread1 = threading.Thread(target=conexion_base_datos)
    thread2 = threading.Thread(target=consulta_servidor_web)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    logging.info('Final del programa, los threads han finalizado')
