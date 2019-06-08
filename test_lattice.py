from lattice import Lattice

def test_lattice_number_neigbors():
  ''' Test the number of neighbors in the lattice.'''

  lattice = Lattice(3,3)

  for place in [(0,0),(0,1),(1,1)]:
    answer = lattice.find_neighbors(place)
    assert len(answer)==4, "Wrong number of neighbors"
  
  assert (2,1) in lattice.find_neighbors((1,1))

  try:
    fail = True
    lattice2 = Lattice(5,1)
  except AssertionError:
    fail = False
  assert not fail
