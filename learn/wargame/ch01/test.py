import random

def reset_position(position_meter):
    position_meter['player'] = [3,0]
    position_meter['enemy'] = [3,3]

def reset_health(health_meter):
    health_meter['player'] = 100
    health_meter['enemy'] = 90

def process_user_move():
    user_choice_x = input("choose x move(1/-1/0)")
    user_choice_y = input("choose y move(1/-1/0)")
    user_move_x = int(user_choice_x)
    user_move_y = int(user_choice_y)
    return user_move_x, user_move_y

def process_computer_choice():
    computer_move_x = random.randint(0,0)
    computer_move_y = random.randint(0,0)
    return computer_move_x, computer_move_y

def update_move(before_move, move):
    after_move = before_move + move
    if after_move > 5: 
        after_move = 5
    if after_move < 0:
        after_move = 0
    return after_move

def update_position(position_meter):

    user_move_x, user_move_y = process_user_move()
    computer_move_x, computer_move_y = process_computer_choice()
    user_position_x, user_position_y= position_meter['player']
    computer_position_x, computer_position_y= position_meter['enemy']
    user_position_x = update_move(user_position_x,user_move_x)
    user_position_y = update_move(user_position_y,user_move_y)
    computer_position_x = update_move(computer_position_x, computer_move_x)
    computer_position_y= update_move(computer_position_y, computer_move_y)


    position_meter['player'] = [user_position_x, user_position_y]  
    position_meter['enemy'] = [computer_position_x, computer_position_y]


    print("player is in %d : %d" %(user_position_x,user_position_y))
    print("enemy is in %d : %d" %(computer_position_x,computer_position_y))

    return position_meter

    

def attack(health_meter):
    
    hit_list = 4*['player'] + 6*['enemy']
    injury_unit = random.choice(hit_list)
    injury = random.randint(20,35)
    injury_point = health_meter[injury_unit]
    health_meter[injury_unit] = max(0, injury_point-injury)
    print(health_meter)


def play_game(health_meter,position_meter):
    position_meter_update = {}
    while position_meter['player'] != position_meter['enemy']:
        position_meter = update_position(position_meter)
    print('Enemy Sighted!!')
    continue_attack = True

    while continue_attack:
        continue_attack = input('...continue attack? ')
        if continue_attack == 'n':
            print('Game Over')
            break
        attack(health_meter)

        if health_meter['player'] <= 0:
            print('You Lost')
            break
        if health_meter['enemy'] <= 0:
            print('You Win')
            break

    




def run_application():
    keep_playing = 'y'
    health_meter = {}
    position_meter = {}
    reset_health(health_meter)
    reset_position(position_meter)

    while keep_playing == 'y':
        reset_health(health_meter)
        reset_position(position_meter)
        play_game(health_meter,position_meter)
        keep_playing = input("play again? ")



if __name__ == '__main__':
    run_application()

