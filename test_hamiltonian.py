from numpy import ones,tile,eye
from lattice import Lattice
from hamiltonian import Hamiltonian

def test_energy_ferro():
  ''' Check the energy of the ferromagnetic state.'''

  size = 4
  coupling = 1.0

  lattice = Lattice(size,size)
  ham = Hamiltonian(lattice,coupling)

  assert ham.energy(ones((size,size),dtype=bool)) == 2*coupling*size*size, "Energy of ferromagnetic state is incorrect."

def test_energy_antiferro():
  ''' Check the energy of the antiferromagnetic state.'''

  size = 10
  coupling = 1.0

  lattice = Lattice(size,size)
  ham = Hamiltonian(lattice,coupling)
  
  afm = tile(eye(2,dtype=bool),(5,5))

  assert ham.energy(afm) == -2*coupling*size*size, "Energy of antiferromagnetic state is incorrect."
