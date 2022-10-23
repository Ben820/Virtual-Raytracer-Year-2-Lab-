# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:06:42 2019

@author: 44743
"""
"""
A function which calculates the x and y positions traced out by a bundle of 
uniformly distributed, collimated rays.

Parameters--
R           is the radius of the bundle
sf          is a scaling factor to determine the number of rays in the bundle
rings       is the number of rings the bundle has
base_factor is the starting number of rays per ring in the bundle

Returns--
list_points     is the list of x and y points the rays in the bundle start from
"""
import numpy as np
import Raytracer as rt
import matplotlib.pyplot as plt

def Bundle(R, sf, rings, base_factor):
    radius = R
    scaling_factor = sf
    number_rings = rings
    set_points = np.array(base_factor) 

    # Spacing between consecutive rings.
    ring_spacing = (radius)/(number_rings)    
    
    points_per_ring = (set_points)*(scaling_factor)

    initial_points = np.arange(0, radius, ring_spacing)
    
    # list_points is used for Bundler function
    # list_x and list_y are used for plotting spot diagram at input plane
    list_points = []
    list_x = []
    list_y = []
    
    for i in range(0, number_rings): 
        # A is the ith point along the x axis.
        A = initial_points[i]
        
        if A == initial_points[0]:
            points_per_ring[0] = 1
            list_x.append(0)
            list_y.append(0)
            list_points.append(np.array([0, 0, 0]))
        
        else:
            n = points_per_ring[i]
            # Number of points in the ith ring
        
            for k in range(1,(n+1)):
                #Distributes the points evenly around the ring
                phi = (2*k*(np.pi))/n
                xcoord = A*(np.cos(phi))
                ycoord = A*(np.sin(phi))
                
                S = np.array([xcoord, ycoord, 0])
                list_x.append(xcoord)
                list_y.append(ycoord)
                list_points.append(S)

    #plt.plot(list_x, list_y, '.')
    #plt.grid()
    #plt.xlabel(" x component of ray / mm ")
    #plt.ylabel(" y component of ray / mm ")
    #plt.title(" Spot diagram for beam with diameter 10 mm at input plane z = 0 """)
    #plt.show()
    return list_points

#%%
A = Bundle(12, 10, 6, [0,1,2,3,4,5])

#%%  

"""Bundler function creates the bundle of rays from a list of x and y coords

Parameters--
listOfPoints    is the list of x and y coordinates of the rays in the bundle
k_direction     is the direction of the bundle; must be the same for the beam 
                to be collimated

Returns--
Bundle      is the bundle of rays; forms a beam
"""

def Bundler(listOfPoints, k_direction):
    Bundle = []
    
    # Appends the initialised rays to the empty list Bundle
    for i in listOfPoints:
         r = rt.Ray(i, k_direction)
         Bundle.append(r)
    return Bundle
    

            

 