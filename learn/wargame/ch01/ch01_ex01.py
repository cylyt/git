import random

def reveal_occupants(idx,huts):
    print('revealing the occupants...')
    msg = ''
    for i in range(len(huts)):
        occupant_info = "<%d : %s>" %(i+1,huts[i])
        msg += occupant_info + " "
    print("\t" + msg)
    print_dotted_line()

def create_huts():
    huts = []
    occupants = ['enemy', 'frend', 'unoccupant']
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts

def print_dotted_line(width = 72):
    dotted_line = '-' * width
    print(dotted_line)

def process_user_choice():
    msg = 'choose a hut to enter(1-5)'
    user_choice = input('\n'+msg)
    idx = int(user_choice)
    return idx

def show_health(health_meter):
    msg = "Health: Sir Foo: %d, Enemy: %d" \
        % (health_meter['player'], health_meter['enemy'])
    print(msg)

def reset_health(health_meter):
    health_meter['player'] = 40
    health_meter['enemy'] = 30

def attack(health_meter):
    hit_list = 4*['player'] + 6*['enemy']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10,15)
    health_meter[injured_unit] = max(hit_points-injury, 0)
    print('Attack!', end='')
    show_health(health_meter)

def play_game(health_meter):

    huts = create_huts()
    idx = process_user_choice()
    reveal_occupants(idx,huts)
    print("entering hut %d" %idx)
    if huts[idx - 1] != 'enemy':
        print("You Win")
    else:
        print('enemy sighted!!!')
        show_health(health_meter)
        continue_attack = True

        while continue_attack:
            continue_attack = input('......continue attack?')
            if continue_attack == 'n':
                show_health(health_meter)
                print('Game Over')
                break
            attack(health_meter)

            if health_meter['enemy'] <= 0:
                print('Enemy Defended, You Win!')
                break
            if health_meter['player'] <=0:
                print('You Lost! Game Over!')
                break
    print_dotted_line()

def run_application():
    keep_playing = 'y'
    health_meter = {}
    reset_health(health_meter)
    print_dotted_line()

    while keep_playing == 'y':
        reset_health(health_meter)
        play_game(health_meter)
        keep_playing = input("play again? ")

    

if __name__ == '__main__':
    run_application()
    
    

    


