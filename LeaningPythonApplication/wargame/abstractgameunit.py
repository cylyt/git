from abc import ABCMeta,abstractmethod
from gameutils import weighted_random_selection
import random

class AbstractGameUnit(metaclass=ABCMeta):

    def __init__(self,name=''):
        #对象属性，名字，最大血，当前血，属性
        self.name=name
        self.max_hp=0
        self.health_meter=0
        self.unit_type=None
        self.enemy=None

    @abstractmethod
    def info(self):
        pass

    def attack(self,enemy):
        #攻击方法，传入友军和敌军
        injured_unit=weighted_random_selection(self,enemy)
        injured_num=random.randint(10,15)
        injured_unit.health_meter=max(injured_unit.health_meter-injured_num,0)
        print('Attack!!',end=' ')
        self.show_health(end=' ')
        enemy.show_health(end=' ')


    def heal(self,heal_by=2,full_healing=True):
        #治疗方法，只能治疗自己，治疗的数值
        if self.health_meter==self.max_hp:
            return
        if full_healing:
            self.health_meter=self.max_hp
        else:
            self.health_meter=min(self.health_meter+heal_by,self.max_hp)
        print('You are Healed',end=' ')
        self.show_health()
    
    def reset_health(self):
        #重置生命为最大值
        self.health_meter=self.max_hp

    def show_health(self,end='\n'):
        #显示对象当前生命
        msg="Health: %s: %d" %(self.name,self.health_meter)
        print(msg,end=end)

    def run_away(self):
        print("Running Away...")
        self.enemy=None
    
    
