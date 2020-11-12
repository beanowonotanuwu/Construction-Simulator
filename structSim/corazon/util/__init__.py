### IMPORTS                         ###
import os
import typing
### IMPORTS                         ###
class _setpath(object):
    def __init__(self, path, backup=1): self.path, self.back = path, backup
    def __enter__(self): os.chdir(self.path); return self
    def __exit__(self, *argz, **kwargz): os.chdir('..' * self.back)
def setpath(relpath: typing.AnyStr, backup: int): return _setpath(
    relpath, backup
)