import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

class ProcesoFacilito(multiprocessing.Process):
    def __init__(self, daemon, name):
        multiprocessing.Process.__init__(self, daemon=daemon, name=name)

    def run(self):
        logging.info('Este mensaje se crea en un nuevo proceso!')

if __name__ == '__main__':
    proceso_facilito = ProcesoFacilito(False, 'proceso-facilito')
    proceso_facilito.start()
