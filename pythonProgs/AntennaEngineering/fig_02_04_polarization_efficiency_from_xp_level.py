
# Polarization efficiency calculated from relative cross-polar level.
# Complement to Figure 2.4 in Foundations of Antennas by Per-Simon Kildal.
# Relative cross-polar level.
import matplotlib.pyplot as plt
import numpy as np
import cmath
import math
import numpy.matlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import pylab as pl


XP_dB = np.array( np.arange(-40.0 ,0.0 ,0.1))
XP = 10**(XP_dB/10);

# Calculate polarization efficiency.
e_pol = 1/ (1 + XP);
e_pol_dB = 10*np.log10(e_pol);

# plot
f2 = plt.figure(1)
plt.plot(XP_dB, e_pol_dB);
plt.axis([-40, 0, -1, 0]);
plt.xlabel('Relative cross-polar level [dB]');
plt.ylabel('Polarization efficiency [dB]');


plt.show()





