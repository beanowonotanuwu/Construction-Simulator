### IMPORTS                         ###
from os import chdir
from os.path import splitext, exists
from typing import AnyStr, Tuple, Iterable, Any
from json import loads
from unum import units, Unum
### IMPORTS                         ###
Value = None
UnitOfMeasurement = None
### OTHER                               ###
class _setpath(object):
    def __init__(self, path: str, backup: int=1): self.path, self.back = path, backup
    def __enter__(self): chdir(self.path); return self
    def __exit__(self, *argz, **kwargz): chdir('..' * self.back)


def setpath(relpath: AnyStr, backup: int): return _setpath(
    relpath, backup
)
def nn(var: Any): return var == None
def ntn(*vals: Any): return all([not nn(i) for i in vals])
### OTHER                               ###
### CONSTRUCT                           ###
class Blueprint(object):
    def __init__(
        self,
        mass:  Unum=None,
        density: Unum=None,
        volume: Unum=None,
        polarity: Unum=None
        ):
        ## Calcs                            ##
        if nn(mass):
            # checks                            #
            assert ntn(density, volume), "Mass, Density, and Volume cannot all be None"
            # checks                            #
        if nn(density):
            # checks                            #
            assert ntn(mass, volume), "Mass, Density, and Volume cannot all be None"
            # checks                            #
        if nn(volume):
            # checks                            #
            assert ntn(density, mass), "Mass, Density, and Volume cannot all be None"
            # checks                            #
        ## Calcs                            ##
        self.mass, self.density, self.volume = (mass, density, volume)
        self.polarity = polarity

class Construct(object):
    def __init__(self, bp: Blueprint):
        self.bp = bp

    ## Basic Blueprint Properties   ##
    @property
    def density(self) -> Unum:
        """
        Returns the density of the object
        """
        return self.bp.mass / self.bp.volume if nn(self.bp.density) else self.bp.density
    
    @property
    def mass(self) -> Unum:
        """
        Returns the mass of the object
        """
        return self.bp.density * self.bp.volume if nn(self.bp.mass) else self.bp.mass
    
    @property
    def volume(self) -> Unum:
        """
        docstring
        """
        return self.bp.mass / self.bp.density if nn(self.bp.volume) else self.bp.volume
    ## Basic Blueprint Properties   ##
    ## Calculations                 ##
    @staticmethod
    def speed(distance: Unum, time: Unum) -> Unum:
        """
        For calculating speed
        """
        return distance / time

    @classmethod
    def netForce(
        cls,
        mass: Unum=None,
        acceleration: Unum=None,
        distance: Unum=None, time: Unum=None
        ) -> Unum:
        """
        For calculating net force
        """
        return (
            mass if ntn(mass) else cls.mass
        ) * (acceleration if ntn(acceleration) else distance * time)
    ## Calculations                 ##

def load_construct(path: AnyStr):
    ## Checks                       ##
    assert exists(path), 'Path does not exist'
    assert splitext(path)[1] in ('.construct',), "Invalid File extension"
    ## Checks                       ##
    with open(fn, 'r') as f:
        content = loads(f"{{\n{f.read()}\n}}")
        return content
### CONSTRUCT                           ###
fn = r"C:\Users\garza_888516\Desktop\Construction Simulator\Construction-Simulator\structSim\corazon\util\example.construct"
res = load_construct(fn)
print(res)

# print(Construct.speed(20*units.m, 5*units.s))