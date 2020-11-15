### IMPORTS                         ###
from os import chdir
from os.path import splitext, exists
from typing import AnyStr, Tuple, Iterable, Any, Dict
from json import loads
from datetime import date
from unum import units, Unum
### IMPORTS                         ###
Value = None
UnitOfMeasurement = None
Filename = None
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
class Info(object):
    def __init__(
        self,
        author: AnyStr,
        date_: date,
        orginization: AnyStr=None,
        readme: "Filename"=None,
        website: AnyStr=None
        ):
        self.author = author
        self.date = date_
        self.org = orginization
        self.readme = readme
        if ntn(readme):
            with open(readme, 'r') as f: self.readme = f.read()
        self.website = website
    
    def __repr__(self):
        return f"""
        Author: {self.author}
        date: {self.date}
        org: {self.org}
        readme: {self.readme}
        website: {self.website}
        """

class Blueprint(object):
    def __init__(
        self,
        mass:  Unum=None,
        density: Unum=None,
        volume: Unum=None,
        polarity: Unum=None,
        parts: Dict=dict()
        ):
        ## Calcs                            ##
        if nn(mass):
            # checks                            #
            assert ntn(density, volume), "Mass, Density, and Volume; at least 2 cannot be None"
            # checks                            #
        if nn(density):
            # checks                            #
            assert ntn(mass, volume), "Mass, Density, and Volume; at least 2 cannot be None"
            # checks                            #
        if nn(volume):
            # checks                            #
            assert ntn(density, mass), "Mass, Density, and Volume; at least 2 cannot be None"
            # checks                            #
        ## Calcs                            ##
        self.mass, self.density, self.volume = (mass, density, volume)
        self.polarity = polarity
        self.parts = parts

    def __repr__(self):
        return f"""
        mass: {self.mass}
        density: {self.density}
        volume: {self.volume}
        polarity: {self.polarity}
        parts: {self.parts}
        """

class Construct(object):
    def __init__(self, bp: Blueprint, info: Info):
        self.bp = bp
        self.info = info
    
    def __repr__(self):
        return f"""blueprint: {self.bp}\ninfo: {self.info}
        """

    ## Basic Blueprint Properties           ##
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
    ## Basic Blueprint Properties           ##
    ## Calculations                         ##
    @staticmethod
    def speed(distance: Unum, time: Unum) -> Unum:
        """
        For calculating speed
        """
        return distance / time
    ## Calculations                         ##

def load_construct(path: AnyStr) -> Construct:
    ## Checks                               ##
    assert exists(path), 'Path does not exist'
    assert splitext(path)[1] in ('.construct',), "Invalid File extension"
    ## Checks                               ##
    with open(fn, 'r') as f:
        content = loads(f"{{\n{f.read()}\n}}")
        info            = content['info']
        imports         = content['imports']
        struct          = content['struct']
        ## Handle Info                      ##
        author      = info['author']
        date_       = info['date']
        org         = info.get('orginization')
        readme      = info.get('readme')
        website     = info.get('website')       # .get bc it returns None if no key found
        info = Info(author, date_, org, readme, website)
        ## Handle Info                      ##
        ## Handle Imports                   ##
        ### BUG: IMPORT SYSTEM NOT WORKING BUG
        ### BUG: IMPORT SYSTEM NOT WORKING BUG
        ### BUG: IMPORT SYSTEM NOT WORKING BUG
        names = dict()
        # if (isinstance(imports, dict) and (imports != {})):
        #     ct = 0
        #     while ct <= (len(imports) - 1):
        #         print(dir(imports.values()))
        #         path_ = imports.values()[ct].replace(".", "/")
        #         path_ = path_.replace("*", ".")
        #         names[imports.keys()[ct]] = load_construct(
        #             path_
        #         )
        ## Handle Imports                   #
        ## Handle Construction              ##
        mass = struct.get('mass')
        density = struct.get('density')
        volume = struct.get('volume')
        polarity = struct.get('polarity')
        blueprint = Blueprint(mass, density, volume, polarity, names)
        ## Handle Construction              ##
        return Construct(blueprint, info)
### CONSTRUCT                           ###