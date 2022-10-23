# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:17:19 2019

@author: 44743
"""
"""
A class describing ray objects initialised with parameters described below.

Parameters--
pos     is the position of the ray
vec     is the direction vector, k , of the ray
Both are always lists or arrays with 3 elements
"""
#%%
import numpy as np

class Ray:
    def __init__(self, pos = [0, 0, 0], vec = [0, 0, 0]):
        """ Parameters-- 
            
        position of the ray
        direction vector, k , of the ray
        Both are always lists or arrays with 3 elements
        """
        
        # Converts the input parameters to arrays for use in calculations.
        self._position = np.array(pos)
        self._vector = np.array(vec)
        
        # After initialisation, the last position and direction vector are
        # the input parameters. 
        self._lastposition = self._position
        self._lastdirection = self._vector

    def posvec(self):
        """Test function. 
        
        Used to show and verify all positions and direction vectors traced by 
        the ray, for troubleshooting. 
        """
        
        return (self._position, self._vector)

    def append(self, new_p = [0, 0, 0], new_k = [0, 0, 0]):
        """Appends a new position and direction, overwriting the previous array. 
        """
        
        # Converts the input parameters to arrays for use in calculations.
        self._lastposition = np.array(new_p)
        self._lastdirection = np.array(new_k)
        
        # np.vstack lets us append a 1 d array to a multi dimensional array.
        self._position = np.vstack((self._position, self._lastposition))
        self._vector = np.vstack((self._vector, self._lastdirection))

    def vertices(self):
        """Returns all points traced by the ray. """
        
        return (self._position)

    def p(self):
        """Returns latest point traced by ray. """
        
        return self._lastposition

    def k(self):
        """Returns latest direction vector of the ray. """
        
        return self._lastdirection
         



