# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:10:19 2019

@author: 44743
"""
"""
A function to implement the vector form of Snells Law. 

Parameters--
in_k        is the incident ray vector.
surf_norm   is the normal vector to the surface.
n1, n2      are the refractive indices of the two media.

Returns--
v_refract   is the normalised refracted ray. 
"""
#%%

import numpy as np

#w = 1/(np.sqrt(2))

def Snellslaw(n1, n2, in_k = [0, 0, 0], surf_norm = [0, 0, 0]): 
    """ Function returns the refracted ray direction using Snells Law.
    """
    
    incident_vector = np.array(in_k)
    surface_normal = np.array(surf_norm)
    
    # Normalises the incident vector; function requires normalised vectors 
    inc_vec_mag = np.sqrt(np.dot((incident_vector), (incident_vector)))
    norm_inc_vec = (incident_vector)/(inc_vec_mag)
    
    # Normalises the surface normal vector; function requires normalised 
    # vectors 
    surf_norm_mag = np.sqrt(np.dot((surface_normal), (surface_normal)))
    norm_surf_norm = (surface_normal)/(surf_norm_mag)
    
    g = n1/n2
    G = np.square(g)

    cos_theta1 = (np.dot((- norm_surf_norm),(norm_inc_vec)))
    
    if cos_theta1 > 0:
        # One of the conditions set out by the vector form of Snells Law 
        
        # Dummy variables are used to simplify code.
        dummy1 = 1 - (np.square((cos_theta1)))
        
        cos_theta2 = np.sqrt(1 - (G*dummy1))
        
        dummy2 = 1 - (np.square((cos_theta2)))
        
        sin_theta1 = (np.sqrt(dummy2))/g
        
        dummy3 = (g*(cos_theta1)) - (cos_theta2)
        
        # v_refract is the unit vector for the refracted ray
        v_refract = (g*(norm_inc_vec)) + (dummy3)*(norm_surf_norm)
        
        if sin_theta1 > (1/g):
            # One of the conditions set out by the vector form of Snells Law
            
            return None
        
        else: 
            return v_refract 
            
    else:
        return None
