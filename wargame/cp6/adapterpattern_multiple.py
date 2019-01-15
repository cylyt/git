class FooElf:

    def leap(self):
        print('FooElf.leap')

    def hit(self):
        print('FooElf.hit')

class ForeignUnitAdapter:

    def __init__(self,adaptee):
        self.foreign_unit=adaptee

    def __getattr__(self,item):
        return getattr(self.foreign_unit,item)

    def set_adapter(self,name,adaptee_method):
        setattr(self,name,adaptee_method)

if __name__=='__main__':
    foo_elf=FooElf()
    foo_elf_adapter=ForeignUnitAdapter(foo_elf)

    foo_elf_adapter.set_adapter('jump',foo_elf.leap)
    foo_elf_adapter.set_adapter('attack',foo_elf.hit)

    foo_elf_adapter.attack()
    foo_elf_adapter.jump()
