class Knight():
    
    def __init__(self,name='Knight'):
        self.name=name

class ElfRider():

    def __init__(self,name='ElfRider'):
        self.name=name

class UnitFactory:
    unit_dict={
        'elfrider':ElfRider,
        'knight':Knight
    }

    @classmethod
    def create_unit(cls,unit_type):
        key=unit_type.lower()
        return cls.unit_dict.get(key)()

class Kingdom:
    factory=UnitFactory
    

    def recruit(self,unit_type):
        unit=type(self).factory.create_unit(unit_type)
        self.pay_gold(unit)
        self.update_records(unit)
        return unit

    def pay_gold(self,something):
        print("Gold Paid")

    def update_records(self,something):
        print("update")

if __name__=='__main__':
    k=Kingdom()
    elf_unit=k.recruit('ElfRider')
    print(elf_unit.name)
