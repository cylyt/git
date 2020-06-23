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

    def __init__(self,name,work_time=0):
        super().__init__(name)
        self._work_time = work_time

    @property
    def work_time(self):
        return self._work_time

    @work_time.setter
    def work_time(self, work_time):
        self._work_time = work_time

    def get_salary(self):
        return 150 * self._work_time

class Seller(Employee):

    def __init__(self,name, sell_num=0):
        super().__init__(name)
        self._sell_num = sell_num
    
    @property
    def sell_num(self):
        return self._sell_num
    
    @sell_num.setter
    def sell_num(self,sell_num):
        self._sell_num = sell_num

    def get_salary(self):
        return 1200 + self._sell_num * 0.05

def main():
    emps = [
            Manager('刘备'), Programmer('诸葛亮'),
            Manager('曹操'),Seller('贾旭'),
            Seller('吕布'), Programmer('张辽'), Programmer('赵云')]
    
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.work_time = int(input('输入%s工作时间' %emp.name))
        elif isinstance(emp, Seller):
            emp.sell_num =float(input('请输入%s销售额' %emp.name))
        print ('%s本月工资为: ￥%s元' %(emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()