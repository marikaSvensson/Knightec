import numpy as np


with open("timesteps2.dat", "rb") as f:
    while True:
        line = f.readline()

        if len(line) == 0: # End of file
            break

        print np.genfromtxt(f, names=True, dtype=None, max_rows=int(3))
