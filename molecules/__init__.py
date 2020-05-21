from polyelectrolyte import StarPolyelectrolyte, LinearPolyelectrolyte
from salt import Salt
from _common import registry

class MoleculeFactory():
    def __init__(self, item_list):
        self.registry = {
            'star' : StarPolyelectrolyte,
            'dna' : LinearPolyelectrolyte,
            'salt' : Salt
        }
        self._function = self.registry[item_list['molecule']]
    
    @property
    def molecules(self):
        return self._function(self.item)