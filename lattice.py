import numpy

class Lattice():
  ''' encodes the geometry of the lattice '''
  def __init__(self,Nwidth,Nheight):
    assert Nheight!=1 and Nwidth!=1, "1-d is not implemented."
    self.Nheight = Nheight
    self.Nwidth = Nwidth

  def find_neighbors(self,position):
    ''' return a list of tuples of the nearest neighbors of a tuple/position '''
    # Only implemented for PBC
    return [
        ((position[0]+1)%self.Nwidth,position[1]),
        (position[0],(position[1]+1)%self.Nheight),
        ((position[0]-1)%self.Nwidth,position[1]),
        (position[0],(position[1]-1)%self.Nheight)
      ]
