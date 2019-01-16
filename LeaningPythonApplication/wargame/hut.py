class Hut():
    
    def __init__(self,number,occupant):
        #房子的序号，占领者,是否占领过
        self.occupant=occupant
        self.number=number
        self.is_acquired=False

    def acquire(self,new_occupant):
        #更新占领状态
        self.occupant=new_occupant
        self.is_acquired=True
        print("GOOD JOB!! Hut %d is acquired" %self.number)

    def get_occupant_type(self):
        if self.is_acquired:
            occupant_type='Acquired'
        elif self.occupant is None:
            occupant_type='Unoccupied'
        else:
            occupant_type=self.occupant.unit_type
        return occupant_type




