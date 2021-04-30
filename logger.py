from enum import Enum

from logging import getLogger, StreamHandler, Formatter
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

class Level(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

class Logger:
    def __init__(self, level):
        
        # select level
        self.level = INFO
        if level == Level.DEBUG:
            self.level = DEBUG
        elif level == Level.INFO:
            self.level = INFO
        elif level == Level.WARNING:
            self.level = WARNING
        elif level == Level.ERROR:
            self.level = ERROR
        elif level == Level.CRITICAL:
            self.level = CRITICAL
        
        # set Logger and set level
        self.logger = getLogger(__name__)
        self.logger.setLevel(self.level)        
        
        # get hander and set level
        self.handler = StreamHandler()        
        self.handler.setLevel(self.level)
        
        # set formatte
        f = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.handler.setFormatter(Formatter(f))
        
        # add handler to logger
        self.logger.addHandler(self.handler)
        self.logger.propagate = False
    
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
