from knight import Knight
from orcrider import OrcRider
from hut import Hut
from gameutils import print_dotted_line

import random

class AttackOfTheOrcs:

    def __init__(self):
        self.huts=[]
        self.player=None

    def show_game_mission(self):
        print("Mission:")
        print("  1. Fight with the enemy.")
        print("  2. Bring all the huts in the village under your control")
        print_dotted_line

    def get_occupants(self):
        return [x.get_occupant_type() for x in self.huts]


    def proess_play_choice(self):
        verifying_choice=True
        idx=0
        print("Current occupants: %s" %self.get_occupants())
        while verifying_choice:
            play_choice=input('Choose a hut number to enter (1-5):')
            idx=int(play_choice)-1

            if self.huts[idx].is_acquired:
                print("you have entered this hut, try again")
            else:
                verifying_choice=False
        return idx

    def _occupy_huts(self):
        for i in range(5):
            choice_list=['enemy','friend',None]
            computer_choice=random.choice(choice_list)
            if computer_choice=='enemy':
                name='enemy-'+str(i+1)
                self.huts.append(Hut(i+1,OrcRider(name)))
            elif computer_choice=='friend':
                name='knight-'+str(i+1)
                self.huts.append(Hut(i+1,Knight(name)))
            else:
                self.huts.append(Hut(i+1,computer_choice))
        

    def play(self):
        self.player=Knight()
        self._occupy_huts()

        self.show_game_mission()
        self.player.show_health()

        acquire_num=0
        
        while acquire_num<5:
            idx=self.proess_play_choice()
            self.player.acquire_hut(self.huts[idx])

            if self.player.health_meter<=0:
                print("You Lose.")
                break

            if self.huts[idx].is_acquired:
                 acquire_num+=1

        if acquire_num==5:
            print("Congratulations! You Win!!!")

           
if __name__ == "__main__":
    game=AttackOfTheOrcs()
    game.play()
