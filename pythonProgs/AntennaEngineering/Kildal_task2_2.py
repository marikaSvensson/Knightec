import matplotlib.pyplot as plt
import numpy as np
import cmath
import math
import numpy.matlib

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import pylab as pl


# -------------------- define vectors -------------
A_dB = np.array( np.matlib.repmat(np.arange(0.0,10.0,0.02) -5.0, 1, 1 ))
Delta_phi_deg  = np.array(np.matlib.repmat( np.arange(0.0,50.0,0.1)-25 ,1,1))	
Delta_phi_deg_pure  = np.arange(0.0,50.0,0.1)-25	

print Delta_phi_deg_pure
A =  10**(A_dB/20)

# co and cross polar
N = len(A[0,:])
M = N 
E_co =(1.0 + np.transpose(A)*np.exp( (Delta_phi_deg*math.pi*1j/180) ) )/math.sqrt(2) 
E_xp =(1.0 - np.transpose(A)*np.exp( (Delta_phi_deg*math.pi*1j/180) ) )/math.sqrt(2) 

# Rel cross polar level
XP  = np.array( abs(np.divide(E_xp, E_co))**2 )
XP_dB = np.array( 10*np.log10( XP) )

# size of array 
print XP_dB.shape 
print A_dB.shape


#------------------------ plotting ----------------
f1 = plt.figure(1)


print Delta_phi_deg_pure[250:255]
ind = (np.argwhere(Delta_phi_deg_pure <= 0.2))[-1,0]
print   ind
print Delta_phi_deg_pure[ind]

if (1):
	plt.plot(A_dB[0,:], XP_dB[ind,:])
	plt.ylabel('X_dB [dB]')
	plt.axis([A_dB[0,1], A_dB[0,-1], -40, 0])
	#plt.show()	

	#-------------------------------------------------
	# Plot XP level as a function of phase error.
	f2 = plt.figure(2)
	irow = np.argwhere(A== 1.0)[0,-1];  # amplitude==1
	print np.argwhere(A== 1.0)
	print irow
	
	plt.plot(Delta_phi_deg[0,:], XP_dB[irow,:]);

	plt.axis([0.0, 10.0, -40.0, 0.0]);
	plt.xlabel('Phase error [deg]');
	plt.ylabel('Relative cross-polar level [dB]');

	#--------------
 plot ----------------------------------
	f3 = plt.figure('surf')
	ax = f3.gca(projection='3d')	

	# Plot both amplitude and phase error
	Delta_phi_deg_plot, A_dB_plot = np.meshgrid(Delta_phi_deg[0,:], A_dB[0,:])
	surf = ax.plot_surface( Delta_phi_deg_plot, A_dB_plot, XP_dB,cmap=cm.coolwarm,linewidth=0, antialiased=False );

	plt.title('Relative cross-polar level [dB]');
	plt.xlabel('Phase error [deg]');
	plt.ylabel('Amplitude error [dB]');

	ax.set_zlim(-40, 1.0)
	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
	# Add a color bar which maps values to colors.
	f3.colorbar(surf, shrink=0.5, aspect=5)

	# contour plot:
	f4 = plt.figure('contour')
	plt.contour(Delta_phi_deg_plot*math.pi/180, A_dB_plot, XP_dB)
	plt.axis([-1.0, 1.0, -5, 5]);
	plt.show()


