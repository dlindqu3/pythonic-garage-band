 
from socketserver import DatagramRequestHandler


class Musician(): 
  def __init__(self, name, instrument): 
    self.name = name 
    self.instrument = instrument 
    def __str__(self): 
      pass 
    def __repr__(self): 
      pass
    def play_solo(): 
      return f'currently playing {self.instrument}'


class Band(Musician): 
  instances = []
  def __init__(self, name, members=None): 
    if members is None: 
      members = []
    self.members = members
    self.name = name
    Band.instances.append(self)
  @classmethod
  def to_list(cls): 
    return cls.instances
  def play_solos(self): 
    solos = []
    for musician in self.members: 
      solos.append(musician.play_solo())
    return solos
  

the_nobodies = Band("The Nobodies")
print(Band.instances)

# nirvanna = Band('Nirvana', ['kurt', 'dave', 'billy'])

class Guitarist(Musician): 
  def __init__(self, name): 
    self.name = name 
    self.instrument = "guitar"
  def get_instrument(self): 
    return self.instrument
  def play_solo(self): 
    return "face melting guitar solo"
  def __str__(self): 
    return f"My name is {self.name} and I play {self.instrument}"  
  def __repr__(self):
    return f"{self.__class__.__name__} instance. Name = {self.name}"   

# guitarist1 = Guitarist('Kurt')
# nirvanna = Band('Nirvanna', [guitarist1])

class Drummer(Musician): 
  def __init__(self, name): 
    self.name = name 
    self.instrument = "drums"
  def get_instrument(self): 
    return self.instrument
  def play_solo(self): 
    return "rattle boom crash"
  def __str__(self): 
    return f"My name is {self.name} and I play {self.instrument}" 
  def __repr__(self):
    return f"{self.__class__.__name__} instance. Name = {self.name}"


class Bassist(Musician): 
  def __init__(self, name): 
    self.name = name 
    self.instrument = "bass"
  def get_instrument(self): 
    return self.instrument
  def play_solo(self): 
    return  "bom bom buh bom"
  def __str__(self): 
    return f"My name is {self.name} and I play {self.instrument}" 
  def __repr__(self):
    return f"{self.__class__.__name__} instance. Name = {self.name}"

# kurt = Guitarist("Kurt Cobain")
# krist = Bassist("Krist Novoselic")
# dave = Drummer("Dave Grohl")

# nirvana_members = [kurt, krist, dave]
# nirvana = Band("Nirvana", nirvana_members)