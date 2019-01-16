import textwrap
import random

def print_dotted_line(self,width=72):
    print("-"*width)

def weighted_random_selection(obj1,obj2):
    weighted_list=4*[id(obj1)]+6*[id(obj2)]
    selection=random.choice(weighted_list)

    if selection==id(obj1):
        return obj1
    return obj2

def show_theme_message(width=72):
    print_dotted_line
    print("Attack of The Orcs v0.0.1:")
    msg=(
        "The war between humans and their arch enemies,Orcs,was in the "
        "offing.Sir Foo, one of the brave knights guarding the southern"
        "plains began a long journey towards the east through an unknown"
        "dese forest. On his way, he spotted a small isolated settlement."
        "Tired and hoping to replenish his food stock,he decide to take "
        "a detour. As he approached the village,he saw five huts. There "
        "was no one to be seen around. Hesitantly, he decided to enter...")

    print(textwrap.fill(msg,width))