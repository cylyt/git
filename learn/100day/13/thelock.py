from time import sleep
from threading import Thread

class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        new_balance = self._balance + money
        sleep(0.01)
        self._balance = new_balance

    @property
    def banlance(self):
        