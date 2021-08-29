
import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\dir_Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%d-%m-%Y %H:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
