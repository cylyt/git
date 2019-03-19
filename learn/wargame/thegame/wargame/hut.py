class Hut:

    def __init__(self,number,occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False
    
    def acquire(self,new_occupant):
        self.occupant = new_occupant
        self.is_acquired = True
        print("Good Job! Hut %d is acquired" %self.number)

    
    def get_occupants_type(self):
        
        if self.is_acquired:
            occupant_type = 'Acquried'
        elif self.occupant is None:
            occupant_type = 'unoccupied'
        else:
            occupant_type = self.occupant.unit_type
        
        return occupant_type

