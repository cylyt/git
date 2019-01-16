class ElfRider:
    def jump(self):
        print("jump inside ElfRider")

class WoodElf:
    def leap(self):
        print("jump inside WoodElf")
    def climb(self):
        print("climb inside WoodElf")

class MountainElf:
    def spring(self):
        print("spring inside MountainElf")

class ForeignUnitAdapter:
    def __init__(self,adaptee,adaptee_method):
        self.foreign_unit=adaptee
        self.jump=adaptee_method

    def __getattr__(self,item):
        return self.climb()
        #return getattr(self.foreign_unit,item)

if __name__=='__main__':
    elf=ElfRider()
    elf.jump()

    wood_elf=WoodElf()
    wood_elf_adapter=ForeignUnitAdapter(wood_elf,wood_elf.leap)
    wood_elf_adapter.jump()
    wood_elf_adapter.climb()

    mountain_elf=MountainElf()
    mountain_elf_adapter=ForeignUnitAdapter(mountain_elf,mountain_elf.spring)

    mountain_elf_adapter.jump()
