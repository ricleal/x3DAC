'''
Created on Oct 22, 2014

@author: rhf


Logger configuration

'''


import json

# import sys
# print(sys.version)

from common import findFileInTheProject
import logging.config

logger = logging.getLogger(__name__)

DEFAULT_LOG_FILENAME = 'logging.json'


def setup_logging(default_path=DEFAULT_LOG_FILENAME):
    """
    Setup logging configuration
    """
    path = findFileInTheProject(default_path)
    with open(path, 'rt') as f:
        jsonConfig = json.load(f)
    logging.config.dictConfig(jsonConfig)
    logger.info("Using logger config file: " + path)


    
