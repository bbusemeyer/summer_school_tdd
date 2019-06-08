from numpy import ones
from lattice import Lattice
from hamiltonian import Hamiltonian

def test_energy_ferro():
  ''' Check the energy of the ferromagnetic state.'''

  size = 10
  coupling = 1.0

  lattice = Lattice(size,size)
  ham = Hamiltonian(lattice,coupling)

  assert ham.energy(ones((size,size),dtype=bool)) == 2*coupling, "Energy of ferromagnetic state is incorrect."
