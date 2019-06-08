import numpy
from lattice import Lattice

class Hamiltonian():
  ''' encodes the spin-spin interactions '''
  def __init__(self,my_lattice,coupling):
    self.lattice = my_lattice
    self.coupling = coupling
  
  def energy(self,spin_state):
    ''' calculates the energy of a spin-state for this Hamiltonian '''
    en = 0
    for i in range(self.lattice.Nwidth):
      for j in range(self.lattice.Nheight):
        for nbr in self.lattice.find_neighbors((i,j)):
          en += self.coupling/2.0
    return en

