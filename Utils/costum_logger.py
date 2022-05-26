import inspect
import logging

def customLogger(logLevel):
    # Obtiene la clase  / metodo del metod que lo llamado
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # Mensaje por defecto
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("vecindario.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger