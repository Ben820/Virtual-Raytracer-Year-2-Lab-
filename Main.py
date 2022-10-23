# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:29:42 2019

@author: 44743
"""
"""
Main script for Optical ray project; split into three sections:
I.      Tester code for single rays - for locating paraxial focal point.
II.     Beam code - propagates beams through the system; produces spot diagram at 
        paraxial focal plane.
III.    General code - propagates multiple rays through system; produces ray 
        diagram. 
"""
#%%
""" I. Tester code """ # for task 15, outputplane = 198.4527

import matplotlib.pyplot as plt
import Raytracer as rt
import OpticalElement as oe

# Initialises required objects 
r = rt.Ray([-0.1, 0, 0],[0, 0, 1])
r2 = rt.Ray([0.1, 0, 0], [0, 0, 1])
item1 = oe.SphericalRefraction(100, 0, 1, 1.5168, 11)
item2 = oe.SphericalRefraction(105, -0.02, 1.5168, 1, 11)
output_plane = oe.OutputPlane(250)

item1.propagate_ray(r)
item1.propagate_ray(r2)
item2.propagate_ray(r)
item2.propagate_ray(r2)
output_plane.propagate_ray(r)
output_plane.propagate_ray(r2)

ver = r.vertices()
ver2 = r2.vertices()

# Plots x components of ray against z components 
plt.plot(ver[:,2], ver[:,0])
plt.plot(ver2[:,2], ver2[:,0])
plt.plot(ver[:,2], ver[:,0], "x")
plt.plot(ver2[:,2], ver2[:,0], "x")
plt.xlim(0,500)
plt.grid()
plt.show()

#%%
""" II. Beam code """

import numpy as np
import matplotlib.pyplot as plt
import OpticalElement as oe
import Bundle as bnd

# Creates bundle and nests the output of Bundle within the parameter for 
# Bundler. 
#
#listOfRays is the Beam
listOfRays = bnd.Bundler((bnd.Bundle(1, 10, 6, [0,1,2,3,4,5])),[0, 0, 1])

# Initialises required objects 
item1 = oe.SphericalRefraction(100, 0, 1, 1.5168, 11)
item2 = oe.SphericalRefraction(105, -0.02, 1.5168, 1, 11)
output_plane = oe.OutputPlane(201.74878083)

vers = []
for r in listOfRays:
    # Propagates Beam of rays through system
    # This selects the last points traced by each ray and appends them to vers
    item1.propagate_ray(r)
    item2.propagate_ray(r)
    output_plane.propagate_ray(r)
    ver = r.vertices()
    
    # the element of ver to be appended needs to match the number of intercepts.
    # e.g. if there are four positions of the ray, the number is 3
    vers.append((ver)[3,:])

# X and Y are the entire x and y components of the array vers, enabling them to 
# be plotted against one another
X = np.array(vers)[:,0]
Y = np.array(vers)[:,1]

""" RMS code
Calculates the RMS of the spot diagram
"""

# The radius is given by pythagoras, (x^2 + y^2)^0.5 hence 
# radius squared = sum of the squares.
radius_squared = (np.square(X)) + (np.square(Y))
mean_square = np.mean(radius_squared)
RMS = np.sqrt(mean_square)
print(RMS) 

#RMS = 0.07111646476532252        
# Diameter of spot diagram is roughly 0.212
# Diameter of geometrical focus is 0.14223292953064504   
# When output plane @ z = 200 , Bundle(10, 10, 5), 
# When item1 = oe.SphericalRefraction(100, 0.03, 1, 1.5, 50)

# Plots spot diagram of beam at the paraxial focal plane.
plt.plot(X,Y, '.')
plt.xlabel("focus")
plt.ylabel("y axis")
plt.title("Spot diagram at paraxial focal plane \n for a Plano-Convex lens and beam diameter 5 mm")
plt.grid()
plt.show()
#%%
""" III. General code
"""

import matplotlib.pyplot as plt
import Raytracer as rt
import OpticalElement as oe

for i in range(-10, 11): 
    r = rt.Ray([i ,0, 0], [0, 0, 1])
    item1 = oe.SphericalRefraction(100, 0, 1, 1.5168, 5)
    
    item2 = oe.SphericalRefraction(105, -0.02, 1.5168, 1, 5)
        # The z position of item 2, if in tandem they model a single convex 
        # lens: 2*(1/cur) + z0 , where z0 is intercept for item 1 """
        
    output_plane = oe.OutputPlane(198.453)
    
    # Propagates set of rays through system
    item1.propagate_ray(r)
    if r._lastposition is None: 
        continue 
    item2.propagate_ray(r)
    output_plane.propagate_ray(r)
    
    ver = r.vertices()
    
    # Plots a ray diagram 
    plt.plot(ver[:,2], ver[:,0])
    plt.plot(ver[:,2], ver[:,0], ".")
    
plt.xlim(0,250)
plt.xlabel("Optical axis; Paraxial focal plane z = 201.749 mm")
plt.ylabel("x axis")
plt.title("Ray diagram diagram for plano-convex surface")
plt.grid()
plt.show()
