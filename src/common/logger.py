'''
Created on Oct 22, 2014

@author: rhf
'''

import os
import json

import sys
print(sys.version)

import logging
import logging.config

logger = logging.getLogger(__name__)

DEFAULT_LOG_FILENAME = 'logging.json'


def setupLogging(default_path=DEFAULT_LOG_FILENAME):
    """
    Setup logging configuration
    """
    path = findFileInTheProject(default_path)
    with open(path, 'rt') as f:
        jsonConfig = json.load(f)
    logging.config.dictConfig(jsonConfig)
    logger.info("Using logger config file: " + path)

def findFileInTheProject(fileName):
    """
    Attempts to locate a filename inside the project
    
    @return: the complete path of the file found
    """
    fileNameAttempt = os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)
    if os.path.exists(fileNameAttempt):
        return fileNameAttempt
    
    fileNameAttempt = os.path.join(os.getcwd(),fileName)
    if os.path.exists(fileNameAttempt):
        return fileNameAttempt
    
    fileNameAttempt = os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)
    if os.path.exists(fileNameAttempt):
        return fileNameAttempt
    
    fileNameAttempt = os.path.join(os.getcwd(),os.path.join(os.pardir,fileName))
    if os.path.exists(fileNameAttempt):
        return fileNameAttempt
    
    fileNameAttempt = os.path.join(os.getcwd(),"../",os.path.join(os.pardir,fileName))
    if os.path.exists(fileNameAttempt):
        return fileNameAttempt
    
    raise IOError("File not found in the Project: "+fileName)
    
