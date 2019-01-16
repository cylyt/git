import math
import random
import time
class GoldHunt:

    def __init__(self,field_coins=5000,field_radius=10.0,
                search_radius=1.0):
        self.field_coins=field_coins
        self.field_radius=field_radius
        self.search_radius=search_radius

        self.x_ref=-(self.field_radius-self.search_radius)
        self.y_ref=0.0

        self.move_distance=2*self.search_radius


    def play(self):

        total_collected_coins=[]
        x_list,y_list=generate_random_points(self.field_radius,
                                            self.field_coins)
        
        count=0
        while self.x_ref<=9.0:
            count+=1
            coins=self.find_coins(x_list,y_list)
            print("Circle# {num},center:({x},{y}),coins:{gold}".format(
                num=count,x=self.x_ref,y=self.y_ref,gold=len(coins)))
            total_collected_coins.extend(coins)
            self.x_ref+=self.move_distance

        print("Total collected coins: ",len(total_collected_coins))

    def find_coins(self,x_list,y_list):
        #x，y为金币的坐标，ref_x,ref_y为搜索的中心坐标，dist为两点的距离
        collected_coins=[]
        for x,y in zip(x_list,y_list):

            delta_x=self.x_ref-x 
            delta_y=self.y_ref-y
            dist=math.sqrt(delta_x*delta_x+delta_y*delta_y)

            if dist<=self.search_radius:
                collected_coins.append((x,y))

        return collected_coins

def generate_random_points(ref_radius,total_points):
        x=[]
        y=[]
        for i in range(total_points):
            theta=random.uniform(0.0,2*math.pi)
            r=ref_radius*math.sqrt(random.uniform(0.0,1.0))
            x.append(r*math.cos(theta))
            y.append(r*math.sin(theta))
        return x,y   

if __name__=='__main__':
    start=time.perf_counter()
    game=GoldHunt()
    game.play()
    end=time.perf_counter()
    print("Total time interval: ", end-start)

