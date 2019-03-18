import random
from abc import ABCMeta, abstractmethod

def weighted_random_selection(obj1, obj2):
    weight_list = 3*[id(obj1)]+7*[id(obj2)]
    selection = random.choice(weight_list)

    if selection == id(obj1):
        return obj1
    return obj2

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
            self.health_meter =min(self.max_hp, self.health_meter + heal_by)
        print("You Are Healed!", end = '')
        self.show_health()

    def reset_health_meter(self):
        self.health_meter = self.max_hp

    def show_health(self, end = '\n'):
        msg = 'Health: %s: %d' %(self.name, self.health_meter)
        print(msg, end = end) 

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

class OrcRider(AbstractGameUnit):

    def __init__(self, name = ''):
        super().__init__(name = name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        print("I'm a Orc Wolf Rider")

class Hut:

    def __init__(self,number,occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False
    
    def acquire(self,new_occupant):
        self.occupant = new_occupant
        self.is_acquired = True
        print("Good Job! Hut %d is acquired" %self.number)

    
    def get_occupants_type(self):
        
        if self.is_acquired:
            occupant_type = 'Acquried'
        elif self.occupant is None:
            occupant_type = 'unoccupied'
        else:
            occupant_type = self.occupant.unit_type
        
        return occupant_type



class AttackOfTheOres:

    def __init__(self):
        self.huts = []
        self.player = None
    
    def get_occupants(self):
        return [x.get_occupants_type() for x in self.huts]
    
    def _process_user_choice(self):
        verifying_choice = True
        idx = 0
        print("Current occupants: %s" %self.get_occupants())
        while verifying_choice:
            user_choice = input("Choose a hut number to enter:")

            try:
                idx = int(user_choice)
            except ValueError as e:
                print("Invalid input, args: %s \n" %e.args)
                continue
            
            try:
                if self.huts[idx-1].is_acquired:
                    print("you have acquired this hut")
                else:
                    verifying_choice = False
            except IndexError:
                print("Invalid input: ", idx)
                print("Number should be in  the range 1-5")
                continue
        return idx        
    
    def _occupy_huts(self):
        
        for i in range(5):
            choice_list = ['enemy', 'friend', None]
            computer_choice = random.choice(choice_list)
            if computer_choice == 'enemy':
                name = 'enemy-' + str(i+1)
                self.huts.append(Hut(i+1, OrcRider(name)))
            elif computer_choice == 'friend':
                name = 'knight-' + str(i+1)
                self.huts.append(Hut(i+1,Knight(name)))
            else:
                self.huts.append(Hut(i+1,computer_choice))

    def play(self):
        self.player = Knight()
        self._occupy_huts()
        acquired_hut_count = 0

        self.player.show_health()

        while acquired_hut_count < 5:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])

            if self.player.health_meter <= 0:
                print('You Lost')
                break

            if self.huts[idx-1].is_acquired:
                acquired_hut_count += 1
        
        if acquired_hut_count ==5:
            print('You Win!!')



if __name__ == '__main__':
    game = AttackOfTheOres()
    game.play()
