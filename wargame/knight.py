from abstractgameunit import AbstractGameUnit

class Knight(AbstractGameUnit):

    def __init__(self,name='Sir Foo'):
        super().__init__(name=name)
        self.max_hp=40
        self.health_meter=self.max_hp
        self.unit_type="friend"

    def info(self):
        print("I'm a knight")

    def acquire_hut(self,hut):
        print("Entering hut %d....." %hut.number)
        is_enemy=(isinstance(hut.occupant,AbstractGameUnit)
        and hut.occupant.unit_type=='enemy')
        continue_attack='y'
        if is_enemy:
            print('Enemy Sighted!')
            self.show_health(end=' ')
            hut.occupant.show_health(end=' ')
            while continue_attack:
                continue_attack=input('".....continue to attack?(y/n): "')
                if continue_attack=='n':
                    self.run_away()
                    break
                self.attack(hut.occupant)

                if hut.occupant.health_meter<=0:
                    print('Good Job!')
                    hut.acquire(self)
                    break
                
                if self.health_meter<=0:
                    print('Game Over')
                    break
        else:
            if hut.get_occupant_type=='Unoccupied':
                print('Hut is unoccupied')
            else:
                print('Friend Sighted.')
            hut.acquire(self)
            self.heal()


            

        
        
