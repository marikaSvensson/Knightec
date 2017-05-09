from ase import Atoms
from ase.calculators.emt import EMT
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.optimize import QuasiNewton
from ase.constraints import FixAtoms

# -----------------potential energy --------------------
d = 1.0
molecule = Atoms('2N', positions = [(0.,0.,0.), (0.,0.,d)])
molecule.set_calculator( EMT() )

slab = fcc111('Cu', size = (4,4,2), vacuum = 10.0)
slab.set_calculator( EMT() )


e_slab = slab.get_potential_energy()
print(e_slab)
print ("\n")

eN2 = molecule.get_potential_energy()
print(eN2)
print ("\n")



# -----------------structure relaxation--------------

h = 1.85
add_adsorbate(slab, molecule ,h,'ontop')
constraint = FixAtoms(mask = [a.symbol != 'N' for a in slab])
slab.set_constraint(constraint)

dyn = QuasiNewton(slab, trajectory = 'N2CuMarika.traj')
dyn.run(fmax = 0.02)


# --------------- import / outport ------------------------
from ase.io import write
write('slab.xyz', slab)

from ase.io import read
slab_from_file = read('slab.xyz')

# ------------------- visualization ----------------------
from ase.visualize import view
view(slab)

# ------------------  Molecular Dynamics ----------------
from ase.md.verlet import VelocityVerlet
from ase import units

dyn = VelocityVerlet(molecule, dt = 1.0 * units.fs)

for i in range(10):
	pot = molecule.get_potential_energy()
	kin = molecule.get_kinetic_energy()
	print('%2d: %.5f eV, %.5f eV,  %.5f eV '%( i, pot + kin, pot, kin)  )
	dyn.run(steps = 20 ) 



















