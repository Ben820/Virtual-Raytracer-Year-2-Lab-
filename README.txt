README: Sequential Geometrical Optics Ray Tracer. 
This program models a sequential optical ray tracer, using the geometrical model of optics.
The code is run entirely through the Main.py file. 
The modules which are utilised in Main.py are:
Raytracer.py	This contains the Ray class: It is used to initialise ray objects and describe their behaviour. It takes as parameters the initial position and direction of the ray
OpticalElement.py 	This contains the Optical element class and its derived classes and describes how a ray intercepts and propagates through the specified surfaces.
Spherical surfaces are initialised using the following parameters: an intercept with the optical axis, the relevant refractive indices, curvature and aperture.  
Output planes are initialised using only their intercept with the optical axis.
SnellsLaw.py 	This defines the way a Ray object will propagate through an Optical element using the vector form of Snell’s law of refraction. Parameters are the refractive indices of the relevant media, the incident ray vector and the surface normal at the point of intercept. 
Bundle.py 	This outlines the procedure for creating a uniform collimated beam, comprised of multiple rays. 
The first function Bundle creates the uniform beam and takes as parameters the maximum radius of the beam, the spacing between the rings that make the beam, and a scaling factor describing the number of points per ring. 
The second function Bundler creates the collimated beam and has parameters of the output from the Bundle function and the desired direction vector. 
The Graphing.py script is separate. 
Graphing.py	This takes the manually collected data – noted down in the Lab book – and creates the graphs used in the supporting report, along with the Airy radii. 
The Main.py script and the Graphing.py script are enough to reproduce all graphs and results in the project. The Main.py file is split up into three sections.
The first of which, Tester, is done to calculate the paraxial focus point, using two rays very close to the optical axis.
The second, Beam Code, is used to propagate the beam of specified parameters through the ray tracer, is used to calculate the RMS radius, and produces the spot plot diagrams used in the report.
The third, General code, is used to create ray diagrams showing the propagation of a set of rays – NOT a beam – through the system. It is used to verify the conditions for Tester and Beam Code. 


