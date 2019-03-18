import random
from hut import Hut
from knight import Knight
from orcrider import OrcRider

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
