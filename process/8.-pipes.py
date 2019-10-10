import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

# PIPES
# Publisher
# Subscriber

class Publisher(multiprocessing.Process):
    def __init__(self, connection):
        self.connection = connection
        multiprocessing.Process.__init__(self)

    def run(self):
        logging.info('Hola, nos encontramos en el proceso Publisher')

        for x in range(20):
            self.connection.send(f'Hola, desde el proceso publisher, con el valor {x}')

            time.sleep(0.5)

        self.connection.send(None)
        self.connection.close()

        logging.info('Conexión cerrada para publisher')

class Subscriber(multiprocessing.Process):
    def __init__(self, connection):
        self.is_alive = True
        self.connection = connection
        multiprocessing.Process.__init__(self)

    def run(self):
        logging.info('Hola, nos encontramos en el proceso subscriber')

        while self.is_alive:
            result = self.connection.recv()

            self.is_alive = result is not None

            logging.info(result)
        else:
            self.connection.close()
            logging.info('Conexión cerrada para subscriber')

if __name__ == '__main__':
    connection1, connection2 = multiprocessing.Pipe()

    publisher = Publisher(connection1)
    subscriber = Subscriber(connection2)

    publisher.start()
    subscriber.start()
