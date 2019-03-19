import random

def weighted_random_selection(obj1, obj2):
    weight_list = 3*[id(obj1)]+7*[id(obj2)]
    selection = random.choice(weight_list)

    if selection == id(obj1):
        return obj1
    return obj2
