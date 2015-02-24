'''
Created on Feb 24, 2015

@author: leal
'''
import unittest

from geom3 import *


class Test(unittest.TestCase):


    def test_basic_operations(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(3, 2, 1)
        assert Vector3((1, 2, 3)) == v1
        assert Vector3([1, 2, 3]) == v1
        assert Vector3(Point3(1, 2, 3)) == v1
        assert v1 + v2 == Vector3(4, 4, 4)
        assert v1 - v2 == Vector3(-2, 0, 2)
        assert v1 * 3 == Vector3(3, 6, 9)
        assert 3 * v1 == Vector3(3, 6, 9)
        assert v1 / 2.0 == Vector3(0.5, 1, 1.5)
        assert -v1 == Vector3(-1, -2, -3)
        assert v1[0] == 1 and v1[1] == 2 and v1[2] == 3
        assert list(v1) == [1, 2, 3]
        assert str(v1) == "(1.000,2.000,3.000)"
        assert eval(repr(v1)) == v1
        assert v1.dot(v2) == 10
        assert v1.dot(v2) == dot(v1, v2)
        assert v1.cross(v2) == Vector3(-4, 8, -4)
        assert length(unit(Vector3(2, 3, 4))) == 1.0
        assert length(Vector3(2, 3, 4).norm()) == 1.0
    
    def test_on_points(self):
        p1 = Point3(2, 4, 6)
        p2 = Point3(4, 7, 3)
        v1 = Vector3(1, 2, 3)
        assert Point3((2, 4, 6)) == p1
        assert Point3([2, 4, 6]) == p1
        assert Point3(Vector3(2, 4, 6)) == p1
        assert [p1[i] for i in range(3)] == [2, 4, 6]
        assert p1 - p2 == Vector3(-2, -3, 3)
        assert p1 + v1 == Point3(3, 6, 9)
        assert str(p1) == "(2.000,4.000,6.000)"
        assert eval(repr(p1)) == p1
        try:
            p1 + p2
            assert False
        except TypeError: pass
        try:
            3 * p1
            assert False
        except TypeError: pass

    def test_lines_and_rays(self):
        xRay = Ray3(Point3(0, 0, 0), Vector3(1, 0, 0))
        yRay = Ray3((0, 0, 0), (0, 1, 0))
        zRay = Ray3((0, 0, 0), (0, 0, 1))
        assert xRay.pos(1.0) == Point3(1, 0, 0)
        assert xRay.pos(2) == Point3(2, 0, 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()