#!/usr/bin/python

'''
R. M. F. Leal, S. C. M. Teixeira, V. Rey, V. T. Forsyth and E. P. Mitchell, 
*Absorption correction based on a three-dimensional model reconstruction from visual images*, 
J. Appl. Cryst. (2008). **41**, 729-737

@author: ferrazlealrm@ornl.gov

'''
import sys
import logging
import logging.config

__author__ = "Ricardo M. Ferraz Leal"
__copyright__ = "Copyright 2014, ORNL"
__credits__ = ["Ricardo M. Ferraz Leal"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ricardo M. Ferraz Leal"
__email__ = "ferrazlealrm@ornl.gov"
__status__ = "Beta"

#todo : change this
logging.config.fileConfig('../logging.ini')
logger = logging.getLogger()


def main(argv):
    logger.info('Starting...')
    logger.info('End!')

    
if __name__ == '__main__':
    main(sys.argv)