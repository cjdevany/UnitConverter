from abc import ABC, abstractmethod

# Returns array of size 2: 1st index is the value and 2nd index is the unit.
def parseStringToUnit(string):
    return string.split(' ', 2)

class Unit(ABC):  
    def __init__(self, value, unit_lbl):
        self.value = value
        self.lbl = unit_lbl

    def __str__(self):
        return f'{round(self.value, 3)} {self.lbl}'

    @abstractmethod
    def convert(self, convertTo):
        pass

