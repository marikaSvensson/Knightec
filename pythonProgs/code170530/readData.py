import numpy as np

with open("timesteps.dat", "rb") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            # End of file
            break
        # Skip blank lines
        while len(line.strip()) == 0:
            line = f.readline()
        line2_fields = f.readline().split()
        timestep = float(line2_fields[0])
        particles = int(line2_fields[1])
        data = np.genfromtxt(f, names=True, dtype=None, max_rows=particles)

        print("Timestep:", timestep)
        print("Particles:", particles)
        print("Data:")
        print(data)
        print()