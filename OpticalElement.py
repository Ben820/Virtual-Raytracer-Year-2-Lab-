# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:16:21 2019

@author: 44743
"""
"""
A module containing the class OpticalElement and its derived classes 
SphericalRefraction and OutputPlane.

The classes create different optical surfaces used for ray propagation. 
N.B. optical axis is the z axis, by convention 
"""
#%%

import numpy as np
import SnellsLaw as sl

class OpticalElement:
    """Base Class Optical element. """
    
    def propagate_ray(self, ray):
        """Function to raise an error if propagate_ray is not implemented in
        derived classes.
        """
        
        "propagate a ray through the optical element"
        raise NotImplementedError()


class SphericalRefraction(OpticalElement):
    """A derived class describing the interaction of a spherical refracting 
    surface with a ray object.
    """
    
    def __init__(self, z0, cur, n1, n2, a):
        """Forms a spherical surface with the following parameters--
        
        z0  is the intercept of surface with the z axis
        cur is the curvature of the surface
        n1  is the refractive index of the previous medium
        n2  is the refractve index of the surface medium
        a   is the size of the aperture of the surface
        """
        
        self._intercept_z = z0  
        self._curvature = cur
        self._ref_ind1 = n1  
        self._ref_ind2 = n2  
        self._aperture = a   


    def intercept(self, ray):
        """Calculates the first intercept of a ray with the spherical surface, 
        and gives the normal to the surface at that point.
        
        There are three cases to consider; the curvature of the surface is 
        either positive, negative or zero.
        """
        
        if self._curvature != 0:
            
            abs_curvature = np.absolute(self._curvature)
            
            # The radius of curvature is the inverse of the curvature.
            self._curvature_radius = 1/(abs_curvature)
            curvature_radius = self._curvature_radius
            
            if self._curvature < 0:
                centre_curvature = np.array([0, 0, ((self._intercept_z) - (curvature_radius))])
                
            if self._curvature > 0:
                centre_curvature = np.array([0, 0, ((self._intercept_z) + (curvature_radius))])

            r_vector = (ray._lastposition) - (centre_curvature)

            # k_hat is the normalised direction vector of the ray prior to 
            # intercepting the surface
            k_mag = np.sqrt(np.dot((ray._lastdirection),(ray._lastdirection)))
            k_hat = (ray._lastdirection)/(k_mag)

            # To obtain the point of intercept, the distance the ray travelled 
            # from its starting point to the point of intercept is calculated.
            # This uses a quadratic formula, and hence produces two solutions.
            # A is the discriminant.
            # lengthplus and lengthminus are the resepctive solutions. 
            inner_1 = np.dot((r_vector), (k_hat))
            inner_2 = np.dot((r_vector), (r_vector))
            A = (np.square(inner_1)) - ((inner_2) - (np.square(curvature_radius)))

            if A < 0:
                # This would arise when a ray has no intercept with the surface
                print("A is complex")
                return None, None
            
            lengthplus = - (inner_1) + np.sqrt(A)
            lengthminus = - (inner_1) - np.sqrt(A)
            
            # The ray only propagates forward, hence the length must always be
            # positive. There are therefore three cases to consider:
            # I. Only one of lengthplus and lengthminus is positive
            # II. Both solutions are positive
            # III. Both solutions are negative
            
            # Case I. The correct solution is always positive
            #
            # Where there are spherical surfaces with opposite curvatures,
            # the desired lengths are potentially different, and hence are 
            # distinguished. 
            if lengthplus < 0 and lengthminus > 0:
                length_positive_cur = lengthminus
                length_negative_cur = lengthminus
            if lengthminus < 0 and lengthplus > 0:
                length_positive_cur = lengthplus 
                length_negative_cur = lengthplus
            
            # Case II. 
            if lengthplus > 0 and lengthminus > 0: 
                if lengthplus < lengthminus:
                    length_positive_cur = lengthplus
                    length_negative_cur = lengthminus
                    # With a positive curvature, the intercept needs to be the 
                    # first valid intercept with the circle, hence, the minimum 
                    # length.
            
                if lengthminus < lengthplus:
                    length_positive_cur = lengthminus
                    length_negative_cur = lengthplus
                    # With a negative curvature, the intercept needs to be the 
                    # second valid intercept with the circle, hence, the maximum 
                    # length.
                    
            # Case III. 
            if lengthplus < 0 and lengthminus < 0:
                print("length is negative")
                return None, None
    
    
            if self._curvature < 0:
                x = np.array((length_negative_cur)*(k_hat))
                y = (ray._lastposition)
                intersect_cur = x + y
                
                # Calculates the normal vector to the surface at the point
                # of intercept
                a_vector = (intersect_cur) - (centre_curvature)
                a_vec_mag = np.sqrt(np.dot((a_vector),(a_vector)))
                surface_normal = (a_vector)/(a_vec_mag) 
                
                return intersect_cur, surface_normal

            if self._curvature > 0:
                x = np.array((length_positive_cur)*(k_hat))
                y = ray._lastposition
                intersect_cur = x + y
                
                # Calculates the normal vector to the surface at the point
                # of intercept
                a_vector = (intersect_cur) - (centre_curvature)
                a_vec_mag = np.sqrt(np.dot((a_vector),(a_vector)))
                surface_normal = (a_vector)/(a_vec_mag) 
                
                return intersect_cur, surface_normal
            
            # Limits the rays that can enter the surface using the aperture
            distance_from_z = np.sqrt(np.dot((ray._lastposition),(ray._lastposition)))
            if distance_from_z > self._aperture:
                print("Ray terminated; outside aperture Radius")
                return None, None
            
        if self._curvature == 0:
            # The spherical surface becomes a plane surface normal to the 
            # z axis
                    
            # Z is a point on the plane z = z0
            Z = np.array([0, 0, (self._intercept_z)])
            
            P = ray._lastposition
            K = ray._lastdirection
            
            # The normal vector to the plane z = z0 
            n = np.array([0, 0, -1])
            
            # Calculates the intercept of a vector K with a plane with normal n
            Top = (np.dot((Z - P),(n)))
            Bottom = np.dot(K,n)
            d = Top/Bottom
           
            intersect_cur0 = (d*(K)) + P
            
            # Calculates the normal vector to the surface at the point
            # of intercept
            a_vector = np.array([0, 0, -1])
            a_vec_mag = np.sqrt(np.dot((a_vector),(a_vector)))
            surface_normal = (a_vector)/(a_vec_mag) 
                    
            return intersect_cur0, surface_normal

    def propagate_ray(self, ray):
        """This propagates the ray through the surface, using Snells Law """
        
        n1 = self._ref_ind1
        n2 = self._ref_ind2
        in_k = ray._lastdirection
        # Call the results from self._intercept()
        new_position, normal = self.intercept(ray)
        
        # Ensures the correct normal is taken for different curvature cases
        if self._curvature < 0:
            normalA = -(normal)
            
        if self._curvature > 0:
            normalA = normal
            
        if self._curvature == 0:
            normalA = normal
        
        # Uses Snells Law to calculate the refracted ray direction
        new_direction_vector = sl.Snellslaw(n1, n2, in_k, normalA)
        
        if new_position is not None:
            ray.append(new_position, new_direction_vector)
        else:
            return "new_position is None"


class OutputPlane(OpticalElement):
    """A derived class describing the interaction of a ray with a plane surface 
    where no refraction takes place.
    """
    
    def __init__(self, z1):
        """ Initialised with an intercept with the z axis. """
        self._intercept_z1 = z1

    def _intercept(self, ray):
        """Calculates the point of intercept of the ray with the plane surface
        """
        
        # Point on the plane z = z1
        Z1 = np.array([0, 0, (self._intercept_z1)])
        
        P = ray._lastposition
        K = ray._lastdirection
        # The normal vector to the plane.
        n = np.array([0, 0, -1])
        
        # Calculates the intercept of the ray with the plane surface
        Top = (np.dot((Z1 - P),(n)))
        Bottom = np.dot(K,n)
        d = Top/Bottom
        
        intersect_out = (d*(K)) + P
        
        return intersect_out

    def propagate_ray(self, ray):
        """Describes how a ray interacts with the output plane.
        
        The ray intercepts the plane, but is not refracted, hence Snells Law 
        is not used. 
        """
        
        new_position = self._intercept(ray)
        new_direction_vector = (ray._lastdirection)
        
        ray.append(new_position, new_direction_vector)

