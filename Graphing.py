# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:06:32 2019

@author: 44743
"""
"""
Graphing Script for Optical Ray project.

This script is used to plot graphs for use in the report. 
One of these graphs shows the diffraction limit of the code; it does this by
plotting the RMS spot radius and the Airy radius against the beam diameter, and 
looking at the point of intersection. 

Arrays X and Y contain the results of varying the diameter of the incident
Bundle, using the Main script, recording RMS and calculating the Airy radius.
"""

#%%
""" Case A: Convex Plano lens """
import numpy as np
import matplotlib.pyplot as plt

# Array of RMS values
X = np.array([0.009358, 0.0056789, 0.005403, 0.00290125, 0.002760, 0.001162, 0.0003431, 0.0003186, 0.000042])

# Array of beam radii
Y = np.array([5, 4.2858, 4.167, 3.42857, 3.33, 2.5, 1.67, 1.6, 0.83])
Y2 = 2*Y

# Airy radius is 1.22(λf/D)     f = 98.4527
# Only D changes; the top half of the equation is constant = 7.062602887e-2 mm
# D is the beam diameter = Y2
diff_limit = (7.062602887e-2)/(Y2)

# Plots both measures of the spot radius on the same graph
# Intersection is when diffraction limit is reached.
plt.plot(Y2, diff_limit, "-b", label = "Airy disk radius")
plt.plot(Y2, X, "-r", label = "RMS spot radius")
plt.legend(loc = "upper right")
plt.xlabel("Beam diameter /mm")
plt.ylabel("Spot radius /mm")
plt.title("The diameter of an incident beam against \n the spot radius for a Convex Plano lens")
plt.grid()
plt.show()
#%%
""" Case B: Plano Convex lens """

import numpy as np
import matplotlib.pyplot as plt

# Array of RMS values
X = np.array([0.03729, 0.02149, 0.019947, 0.010179, 0.0046116, 0.0042808, 0.00136093, 0.001263, 0.0016784])

# Array of beam radii
Y = np.array([5, 4.167, 4, 3.2, 2.5, 2.4, 1.67, 1.6, 0.83])
Y2 = 2*Y

# Airy radius is 1.22(λf/D)     f = 101.7488
# Only D changes; the top half of the equation is constant = 7.299051917e-2 mm
# D is the beam diameter = Y2
diff_limit = (7.299051917e-2)/(Y2)

# Plots both measures of the spot radius on the same graph
# Intersection is when diffraction limit is reached.
plt.plot(Y2, diff_limit, "-b", label = "Airy disk radius")
plt.plot(Y2, X, "-r", label = "RMS spot radius")
plt.legend(loc = "upper right")
plt.xlabel("Beam diameter /mm")
plt.ylabel("Spot radius /mm")
plt.title("The diameter of an incident beam against \n the spot radius for a Plano Convex lens")
plt.grid()
plt.show()

