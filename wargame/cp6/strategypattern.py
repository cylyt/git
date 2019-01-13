from abc import ABCMeta,abstractmethod
from collections import Callable

class AbstractGameUnit(metaclass=ABCMeta):

    def __init__(self,name,jump_strategy):
        assert(isinstance(jump_strategy,Callable))
        self.name=name
        self.jump=jump_strategy

    @abstractmethod
    def info(self):
        pass

class DwarfFighter(AbstractGameUnit):
    def info(self):
        print("I am a great dwarf")

def can_not_jump():
    print("I can not jump")

def power_jump():
    print("I can jump 100 feet")

def horse_jump():
    print("Jumping my horse")

if __name__=='__main__':
    dwarf=DwarfFighter("Dwarf",can_not_jump)
    print("Dwarf trying to jump")
    dwarf.jump()

    dwarf.jump=power_jump
    dwarf.jump()
    