import random

class parkinglot:
    def __init__(self,sf,ss=(8,12)):
        self.ss=ss
        self.ts=sf//(ss[0]*ss[1])
        self.a_s=list(range(1,self.ts+1))

    def park_car(self,car,s):
        if s not in self.a_s:
            return f"Car with license plate {car.lp} couldnot park un spot{s}.spot occupied"

        self.a_s.remove(s)
        return f"car with license plate {car.lp} parked  sccessfully in spot {s}"
class Car:
    def __init__(self,lp):
        self.lp=lp

    def __str__(self):
        return f"car with license plate {self.lp}" 

def main():
    pl=parkinglot(2000,ss=(10,12))
    cars_list=[Car(str(random.randint(1000000,9999999))) for i in range(20)]


    for j in cars_list:
        if pl.a_s:
            stp=random.choice(pl.a_s)
            print(pl.park_car(j,stp))
        else:
            print("parking lot is full.exiting program")
            break
if __name__==main():
    main()        


