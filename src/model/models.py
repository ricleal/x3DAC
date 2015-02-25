'''
Created on Jan 29, 2015

@author: rhf
'''
from abc import ABCMeta, abstractmethod

import shapely
import shapely.geometry

class IModel(object):
    '''
    Abstract class
    '''
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def intertection_in(self, ray):
        pass


class Cylinder(IModel):
    def __init__( self, base, radius, height):
        """
        base - point
        height - in Y
        """
        self.base = base.buffer(radius)
        h = shapely.geometry.Point(base.x, base.y+height, base.z)
        self.top = h.buffer(radius)
        
        
    def intertection_in(self, ray):
        return self.shape.intersection(ray)

class Sphere(IModel):
    def __init__( self, center, radius):
        self.shape = center.buffer(radius)
        
    def intertection_in(self, ray):
        return self.shape.intersection(ray)
    

    
    
if __name__ == '__main__':
    center = shapely.geometry.Point(0,0,0)
    radius = 10.0
    sphere = Sphere(center, radius)
    
    line = shapely.geometry.LineString([[10,10,5], [0,0,0]])  
    x = sphere.intertection_in(line)
    
    print x