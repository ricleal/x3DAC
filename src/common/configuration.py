'''
Created on Oct 22, 2014

@author: rhf
'''

DEFAULT_CONFIG_FILENAME = 'config.json'

from UserDict import UserDict
import json
from common import findFileInTheProject,singleton

@singleton
class JsonConfigParser(UserDict):
    '''
    Config parser based JSON
    
    '''

    def __init__(self, configFileName = DEFAULT_CONFIG_FILENAME):
        '''
        Constructor
        '''       
        path = findFileInTheProject(configFileName)
        with open(path, 'rt') as f:
            jsonConfig = json.load(f)
        
        UserDict.__init__(self, jsonConfig)
    
    def __getattr__(self, key):
        return self[key]


# EXAMPLE!
if __name__ == '__main__':
    conf = JsonConfigParser()
    print conf['reconstruction']
    conf['reconstruction']["images"] = 10
    print conf.reconstruction
    conf2 = JsonConfigParser()
    print conf2.reconstruction["images"]