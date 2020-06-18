from random import randint

def roll_dice(n=2):
    """roll dice"""
    total = 0
    for i in range(n):
        total += randint(1, 6)
    return total

print (roll_dice())