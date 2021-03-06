import random
from abc import ABCMeta, abstractmethod
from .gameutils import weighted_random_selection
from .gameuniterror import GameUnitError


class AbstractGameUnit(metaclass = ABCMeta):

    def __init__(self,name = ''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    @abstractmethod
    def info(self):
        pass

    def attack(self,enemy):
        injured_unit = weighted_random_selection(self,enemy)
        injury = random.randint(10,15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print('Attack!', end = '')
        self.show_health(end = '')
        enemy.show_health(end = '')

    def heal(self,heal_by = 2, full_healing = True):
        if self.health_meter == self.max_hp:
            return
        
        if full_healing:
            self.health_meter = self.max_hp
        else:
            self.health_meter += heal_by
        
        if self.health_meter > self.max_hp:
            raise GameUnitError("health_meter > max_hp!", 101)

        print("You Are Healed!", end = '')
        self.show_health()

    def reset_health_meter(self):
        self.health_meter = self.max_hp

    def show_health(self, end = '\n'):
        msg = 'Health: %s: %d' %(self.name, self.health_meter)
        print(msg, end = end) 