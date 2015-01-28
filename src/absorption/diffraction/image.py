'''
Created on Jan 28, 2015

@author: rhf
'''

class Image(object):
    '''
    Diffraction Image
    '''
    
    class Reflection(object):
        def __init__(self, x=0, y=0 ,z=0, i=0, sigI=0):
            self.x = x
            self.y = y
            self.z = z
            self.i = i
            self.sigI = sigI
    
    reflections = []

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def create_dummy_reflections_parallel_to_sample(self, distance_from_sample, number_of_reflections):
        pass
    
    def plot(self):
        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
        import numpy as np
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_aspect("equal")
        
        radius = 10
        #draw sphere
        u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
        x=radius*np.cos(u)*np.sin(v)
        y=radius*np.sin(u)*np.sin(v)
        z=radius*np.cos(v)
        
#         for xi,yi,zi in zip(x, y, z):
#             if xi >0: 
#                 ax.scatter(xi, yi, zi)
        ax.scatter(x, y, z)
        

        plt.show()

i = Image()
i.plot()
    
        