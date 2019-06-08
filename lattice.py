import numpy

class Lattice():
  ''' encodes the geometry of the lattice '''
  def __init__(self,Nlength,Nwidth):
    self.Nlength = Nlength
    self.Nwidth = Nwidth

  def find_neighbors(self,position):
    ''' return a list of tuples of the nearest neighbors of a tuple/position '''
    # Only implemented for PBC
    return [(xnew,ynew) for xnew in [(position[0]+1)%self.Nwidth,(position[0]-1)%self.Nwidth] 
        for ynew in [(position[1]+1)%self.Nwidth,(position[1]-1)%self.Nwidth]]




