import matplotlib.pyplot as plt
import numpy as np
import cmath
import math
import numpy.matlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import pylab as pl


from scipy.integrate import quad
# Contour plot, uv-plot, of the co-polar far-field function. 
#
# Complement to Figure 2.11 in Foundations of Antennas by Per-Simon Kildal.

# By Ulf Carlberg and Madeleine Kildal Schilliger.
# Define inputs.
u = np.array( np.matlib.repmat( np.arange(-5,5,0.01)  , 1, 1 ))
v =np.array( np.matlib.repmat( np.arange(-5,5,0.01)  , 1, 1 ))

#uu = np.transpose(u)*v
#vv = np.transpose(u)*v
uu, vv = np.meshgrid(u[0,:], v[0,:]);
w = math.pi/2;
min_dB = -50;

# Calculate.
t = np.array(np.arange( -1, 1, 2.0/400.0 ));
dt = t[1] - t[0];
GH = u*0;

for ii in  range(np.size(u) ):
	GH[0,ii]= dt*np.trapz( np.cos(0.5*math.pi*t)*np.exp(1*(-w*t**2+math.pi*u[0,ii]*t) ))

GH = GH / np.max(abs(GH));

GE = v*0
for ii in range(np.size(v) ):
	    GE[0,ii] = dt * np.trapz(np.exp(1*(-w*t**2+math.pi*v[0,ii]*t)));

	

	

GE = GE/max(abs(GE));
G = np.transpose(GH)*GE;

G_dB = 20*np.log10(np.abs(G) );
print np.shape(G)
print np.shape(G_dB)
print np.shape(uu)
print np.shape(vv)


if (1):
	# Plot a surf plot.
	f3 = plt.figure('surf')
	ax = f3.gca(projection='3d')
	ax.plot_surface(uu, vv, G_dB);
	plt.xlabel('u = \theta cos(\phi) ( \circ)', 'Interpreter', 'tex');
	plt.ylabel('v = \theta sin(\phi) ( \circ)', 'Interpreter', 'tex');

plt.show()


