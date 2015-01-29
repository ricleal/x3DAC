'''
Created on Jan 29, 2015

@author: rhf
'''
from abc import ABCMeta, abstractmethod

from shapely.geometry import Point

class IModel(object):
    '''
    Abstract class
    '''
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def intertection_in(self, Point):
        pass
    
    @abstractmethod
    def intertection_out(self, Point):
        pass




class Cylinder(IModel):
    def __init__( self, center, radius, height):
        #todo
        pass
    
    