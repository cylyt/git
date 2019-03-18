from abstractgameunit import AbstractGameUnit

class Knight(AbstractGameUnit):

    def __init__(self,name = 'Sir Foo'):
        super().__init__(name = name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'
    
    def info(self):
        print("I'm a Knight")

    def acquire_hut(self,hut):
        print("Entering hut %d....." %hut.number, end = ' ')
        is_enemy = (isinstance(hut.occupant, AbstractGameUnit)) and hut.occupant.unit_type == 'enemy'
        continue_attack = 'y'
        if is_enemy:
            print("Enemy Sighted!")
            self.show_health(end = ' ')
            hut.occupant.show_health(end = ' ')
            while continue_attack:
                continue_attack = input("....continue attack?")
                if continue_attack == "n":
                    self.run_away()
                    break
                self.attack(hut.occupant)

                if hut.occupant.health_meter <=0:
                    print("")
                    hut.acquire(self)
                    break
                if self.health_meter <=0:
                    print("")
                    break
        else:
            if hut.get_occupants_type() == 'unoccupied':
                print("Hut is unoccupied")
            else:
                print("Friend sighted!")
            hut.acquire(self)
            self.heal()
        

    def run_away(self):
        print("Running Away.....")
        self.enemy = None