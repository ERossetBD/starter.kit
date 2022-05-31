import logging

class LogConfig:
    # Constructor of the class
    def __init__(self):
        pass
    
    @staticmethod
    def start_logging():
        logging.basicConfig(filename='logs/executeMain.log', format='%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%d/%m/%Y %I:%M:%S', filemode='w', level=logging.INFO)
        logging.info("Démarrage du traitement.")