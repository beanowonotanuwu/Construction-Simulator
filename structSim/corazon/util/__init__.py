### IMPORTS                         ###
from os import chdir
from typing import AnyStr, Tuple, Iterable
from json import loads
from unum import units, Unum
### IMPORTS                         ###
Value = None
UnitOfMeasurement = None
class _setpath(object):
    def __init__(self, path: str, backup: int=1): self.path, self.back = path, backup
    def __enter__(self): chdir(self.path); return self
    def __exit__(self, *argz, **kwargz): chdir('..' * self.back)

class Blueprint(object):
    def __init__(
        self,
        mass:  Unum,
        density: Unum,
        volume: Unum
        ):
        pass
def setpath(relpath: AnyStr, backup: int): return _setpath(
    relpath, backup
)

def load_construct(content: str):
    loads(f"{{{content}}}")