'''
Created on Feb 24, 2015

@author: leal

Geometry module for use with COSC363, 2009.
Defines Vector3, Point3, Line3, and Ray3 classes for
3D geometry.

Adapted from: https://github.com/phire/Python-Ray-tracer

'''
from math import sqrt

epsilon = 1.e-10  # Default epsilon for equality testing of points and vectors

class GeomException(Exception):
    def __init__(self, message=None):
        Exception.__init__(self, message)


#================================================================
#
# Point3 class
#
#================================================================

class Point3(object):
    """
    Represents a Point in 3-space with coordinates x, y, z.
    Note the distinction between vectors and points.
    Points cannot, for example, be added or scaled.
    """
    
    def __init__(self, x, y=None, z=None):
        """
        Constructor takes a Point3, a Vector3, a 3-tuple or
        a 3-list or any other 3-sequence as a sole argument, or
        values x, y and z.
        """
        if y is None and z is None:
            self.x, self.y, self.z = x  # Unpack a 3-sequence into coords 
        else:
            self.x, self.y, self.z = x, y, z  # Constructor taking x, y, z

    def __sub__(self, other):
        """P1 - P2 returns a vector. P - v returns a point"""
        if isinstance(other, Point3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vector3):
            return Point3(self.x - other.dx, self.y - other.dy, self.z - other.dz)
        else:
            return NotImplemented
        
    def __add__(self, other):
        """P + v is P translated by v"""
        if isinstance(other, Vector3):
            return Point3(self.x + other.dx, self.y + other.dy, self.z + other.dz)
        else:
            return NotImplemented

    def __iter__(self):
        """Iterator over the coordinates"""
        return [self.x, self.y, self.z].__iter__()
    
    def __eq__(self, other):
        """Equality of points is equality of all coordinates to within 
       epsilon (defaults to 1.e-10)."""
        return (abs(self.x - other.x) < epsilon and
                 abs(self.y - other.y) < epsilon and
                 abs(self.z - other.z) < epsilon)

    def __ne__(self, other):
        """Inequality of points is inequality of any coordinates"""
        return not self.__eq__(other)
    
    def __getitem__(self, i):
        """P[i] is x, y, z for i in 0, 1, 2 resp."""
        return [self.x, self.y, self.z][i]

    def __str__(self):
        """String representation of a point"""
        return ("(%.3f,%.3f,%.3f)") % (self.x, self.y, self.z)

    def __repr__(self):
        """String representation including class"""
        return "Point3" + str(self)

#================================================================
#
# Vector3 class
#
#================================================================

class Vector3(object):
    """Represents a vector in 3-space with coordinates dx, dy, dz."""
    
    def __init__(self, dx, dy=None, dz=None):
        """Constructor takes a Point3, a Vector3, a 3-tuple or
        a 3-list or any other 3-sequence as a sole argument, or
        values dx, dy and dz."""
        if dy is None and dz is None:
            self.dx, self.dy, self.dz = dx  # Constructor taking pt, vec, list or tuple as arg
        else:
            self.dx, self.dy, self.dz = dx, dy, dz  # Constructor taking x, y, z
                                    
    def __sub__(self, other):
        """Vector difference"""
        return Vector3(self.dx - other.dx, self.dy - other.dy, self.dz - other.dz)

    def __add__(self, other):
        """Vector sum"""
        return Vector3(self.dx + other.dx, self.dy + other.dy, self.dz + other.dz)

    def __mul__(self, scale):
        """v * r for r a float is scaling of vector v by r"""
        return Vector3(scale * self.dx, scale * self.dy, scale * self.dz)

    def __rmul__(self, scale):
        """r * v for r a float is scaling of vector v by r"""
        return self.__mul__(scale)

    def __div__(self, scale):
        """Division of a vector by a float r is scaling by (1/r)"""
        return self.__mul__(1.0 / scale)

    def __neg__(self):
        """Negation of a vector is negation of all its coordinates"""
        return Vector3(-self.dx, -self.dy, -self.dz)

    def __iter__(self):
        """Iterator over coordinates dx, dy, dz in turn"""
        return [self.dx, self.dy, self.dz].__iter__()

    def __getitem__(self, i):
        """v[i] is dx, dy, dz for i in 0,1,2 resp"""
        return [self.dx, self.dy, self.dz][i]

    def __eq__(self, other):
        """Equality of vectors is equality of all coordinates to within 
       epsilon (defaults to 1.e-10)."""
        return (abs(self.dx - other.dx) < epsilon and
                 abs(self.dy - other.dy) < epsilon and
                 abs(self.dz - other.dz) < epsilon)

    def __ne__(self, other):
        """Inequality of vectors is inequality of any coordinates"""
        return not self.__eq__(other)
    
    
    def dot(self, other):
        """The usual dot product"""
        return self.dx * other.dx + self.dy * other.dy + self.dz * other.dz

    def cross(self, other):
        """The usual cross product"""
        return Vector3(self.dy * other.dz - self.dz * other.dy,
                      self.dz * other.dx - self.dx * other.dz,
                      self.dx * other.dy - self.dy * other.dx) 

    def norm(self):
        """A normalised version of self"""
        return self / length(self)
    def __str__(self):
        """Minimal string representation in parentheses"""
        return ("(%.3f,%.3f,%.3f)") % (self.dx, self.dy, self.dz)

    def __repr__(self):
        """String representation with class included"""
        return "Vector3" + str(self)

#================================================================
#
# Line class
#
#================================================================

class Line3(object):
    """A line is defined by two points in space"""
    
    def __init__(self, p1, p2):
        """Constructor takes two points (or anything convertible to Point3)"""
        self.p1 = Point3(p1)
        self.p2 = Point3(p2)
        
    def pos(self, alpha):
        """The position p1 + alpha*(p2-p1) on the line"""
        return self.p1 + alpha * (self.p2 - self.p1)
    
    def repr(self):
        """String representation of a line"""
        return "Line3(%.3g, %.3g)" % (self.p1, self.p2)

#================================================================
#
# Ray class
#
#================================================================
    
class Ray3(object):
    """A ray is a directed line, defined by a start point and a direction"""
    
    def __init__(self, start, direction):
        """
        Constructor takes a start point (or something convertible to point) and 
          a direction vector (which need not be normalised).
        """
        self.start = Point3(start)  # Ensure start point represented as a Point3
        self.dir = unit(Vector3(direction))  # Direction vector

    def pos(self, t):
        """A point on a ray is start + t*dir for t positive."""
        if t >= 0:
            return self.start + t * self.dir
        else:
            raise GeomException("Attempt to obtain point not on ray")

    def __repr__(self):
        return "Ray3(%s,%s)" % (str(self.start), str(self.dir))
    
    
#================================================================
#
# Global functions on points and vectors
#
#================================================================

def dot(v1, v2):
    """Dot product of two vectors"""
    return v1.dot(v2)

def cross(v1, v2):
    """Cross product of two vectors"""
    return v1.cross(v2)

def length(v):
    """Length of vector"""
    return sqrt(v.dot(v))

def unit(v):
    """A unit vector in the direction of v"""
    return v / length(v)

if __name__ == '__main__':
    pass
        
    
    
    

