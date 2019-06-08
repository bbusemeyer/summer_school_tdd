import numpy

class Lattice():
  ''' encodes the geometry of the lattice '''
  def __init__(self,Nheight,Nwidth):
    assert Nheight!=1 and Nwidth!=1, "1-d is not implemented."
    self.Nheight = Nheight
    self.Nwidth = Nwidth

  def find_neighbors(self,position):
    ''' return a list of tuples of the nearest neighbors of a tuple/position '''
    # Only implemented for PBC
    return [(xnew,position[1]) for xnew in [(position[0]+1)%self.Nwidth,(position[0]-1)%self.Nwidth]] + \
      [(position[1],ynew) for ynew in [(position[1]+1)%self.Nheight,(position[1]-1)%self.Nheight]]



