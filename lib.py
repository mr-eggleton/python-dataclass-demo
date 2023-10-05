from datafiles import datafile
from dataclasses import dataclass
from typing import List

from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
  name: str
  lon: float = 0.0
  lat: float = 0.0

  def distance_to(self, other):
    r = 6371  # Earth radius in kilometers
    lam_1, lam_2 = radians(self.lon), radians(other.lon)
    phi_1, phi_2 = radians(self.lat), radians(other.lat)
    h = (sin((phi_2 - phi_1) / 2)**2
      + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
    return 2 * r * asin(sqrt(h))

class Objective(Position):
  name:     str = ""

@datafile("store/quests/{self.name}.json")
class Quest():
  features: List[Objective]
  name:     str = ""
  pass
  
@datafile("store/progress/{self.name}.json")
class Progress():
  name:     str = ""
  pass

  '''
  features: List[Feature] 
  times:    List[int] = field(default_factory=make_blank_times)
  name:     str = ""
  current:  int = 0
  speeds:   Speeds = Speeds() 
  

  #def __post_init__(self):
    #self.times = self.times[:len(self.features)]
  #  pass
    
  @property
  def total(self):
    if len(self.features):
      return self.features[-1].dist_end
    return 0.0

  def remaining(self, dist:float=0.0):
    return self.total - dist

  @property
  def time(self):
    return self.times[self.current]
  
  @time.setter
  def time(self, t:int):
    self.times[self.current] = t
    #print("@time.setter", self.times)
  '''