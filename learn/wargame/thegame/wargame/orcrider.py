from .abstractgameunit import AbstractGameUnit

class OrcRider(AbstractGameUnit):

    def __init__(self, name = ''):
        super().__init__(name = name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        print("I'm a Orc Wolf Rider")