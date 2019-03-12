import random

if __name__ == '__main__':
    keep_playing = 'y'
    occupants = ['enemy', 'frend', 'unoccupant']
    width = 72
    dotted_line = '-' * width
    print('choose a hut')
    print(dotted_line)

while keep_playing == 'y':
    huts = []
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    
    msg = 'choose a hut to enter(1-5)'
    user_choice = input('\n'+msg)
    idx = int(user_choice)

    print('revealing the occupants...')
    msg = ''
    for i in range(len(huts)):
        occupant_info = "<%d : %s>" %(i+1,huts[i])
        msg += occupant_info + " "
    print("\t" + msg)
    print(dotted_line)
    print("entering hut %d" %idx)

    if huts[idx - 1] == 'enemy':
        print("You lose")
    else:
        print("You Win")
    print(dotted_line)
    keep_playing = input("play again? ")


