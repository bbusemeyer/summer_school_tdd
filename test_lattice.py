from lattice import Lattice

def test_lattice_number_neigbors():
  ''' Test the number of neighbors in the lattice.'''

  lattice = Lattice(3,3)

  for place in [(0,0),(0,1),(1,1)]:
    answer = lattice.find_neighbors((1,1))
    assert len(answer)==4, "Wrong number of neighbors"

