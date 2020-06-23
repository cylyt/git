from abc import ABCMeta, abstractmethod

class Employee(object):

    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name
    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):

    def get_salary(self):
        return 15000

class Programmer(Employee):

    def get_salary(self,work_time):
        return 150*work_time 
class Seller(Employee):

    def get_salary(self,)    