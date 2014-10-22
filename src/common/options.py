'''
Created on Oct 22, 2014

@author: rhf
'''

import argparse

def commandLineOptions():
    '''
    Define command line options
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--aaa', help="if args.a ", default='')
    #TODO: Complete
    
    args = parser.parse_args()
    return args

args = commandLineOptions();
