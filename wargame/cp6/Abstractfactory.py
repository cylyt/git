
class IronJacket:
    pass
class PowerSuit:
    pass
class MithrilArmor:
    pass
class GoldLocket:
    pass
class SuperLocket:
    pass
class MagicLocket:
    pass
class DwarfIronJacket:
    pass
class DwarfPowerSuit:
    pass
class DwarfMithrilArmor:
    pass
class DwarfGoldLocket:
    pass
class DwarfSuperLocket:
    pass
class DwarfMagicLocket:
    pass

class AccessoryFactory:
    armor_dict = {
        'ironjacket': IronJacket,
        'powersuit': PowerSuit,
        'mithril': MithrilArmor
    }
    locket_dict = {
        'goldlocket': GoldLocket,
        'superlocket': SuperLocket,
        'magiclocket': MagicLocket
    }

    @classmethod
    def create_armor(cls,armor_type):
        return cls.armor_dict.get(armor_type)()

    @classmethod
    def create_locket(cls,locket_type):
        return cls.locket_dict.get(locket_type)()

class DwarfAccessoryFactory(AccessoryFactory):
    armor_dict = {
        'ironjacket': DwarfIronJacket,
        'powersuit': DwarfPowerSuit,
        'mithril': DwarfMithrilArmor
    }
    locket_dict = {
        'goldlocket': DwarfGoldLocket,
        'superlocket': DwarfSuperLocket,
        'magiclocket': DwarfMagicLocket
    }

class Kingdom:
    factory=AccessoryFactory

    def buy_accessories(self,armor_type,locket_type):
        armor=self.__class__.factory.create_armor(armor_type)
        locket=self.__class__.factory.create_locket(locket_type)
        print("Kingdom armaor:",armor)
        accesories=[armor,locket]
        self.pay_gold(accesories)
        self.update_records(accesories)
        self.print_info(armor,locket)
    
    def pay_gold(self,something):
        print("Gold Paid")

    def update_records(self,something):
        print("update")

    def print_info(self,armor,locket):
        print("Done with shopping in       :", self.__class__.__name__)
        print("  concrete class for armor  :", armor.__class__.__name__)
        print("  concrete class for locket :", locket.__class__.__name__)

class DwarfKingdom(Kingdom):
    factory=DwarfAccessoryFactory #未写其余方法，借用了

if __name__=='__main__':
    print('Buying accessories in default Kingdom...')
    k=Kingdom()
    k.buy_accessories("ironjacket","goldlocket")
    print('-'*56)
    print('Buying accessories in DwarfKingdom...')
    dwarf_kingdom=DwarfKingdom()
    dwarf_kingdom.buy_accessories("ironjacket","goldlocket")
