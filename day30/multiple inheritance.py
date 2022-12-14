class normalroom:
    def calculate(days,rooms,rent):
        if(days==1):
            rent=300*rooms
        elif(days>1 and days<=5):
            rent=250*days*rooms
        else:
            rent=200*days*rooms
        return rent
class ACroom:
    def calculate(days,rooms,rent):
        if(days==1):
            rent=450*rooms
        elif(days>1 and days<=5):
            rent=300*days*rooms
        else:
            rent=250*days*rooms
        return rent
class suiteroom:
    def calculate(days,rooms,rent):
        if(days==1):
            rent=550*rooms
        elif(days>1 and days<=5):
            rent=500*days*rooms
        else:
            rent=450*days*rooms
        return rent
class Hotel:
    def __init__(self,name,address,mobile,days,rooms,a):
        self.name=name
        self.mobile=mobile
        self.address=address
        self.days=days
        self.rooms=rooms
    def display(self):
        if(a==1):
            rent=normalroom.calculate(self.days,self.rooms,0)
        elif(a==2):
            rent=ACroom.calculate(self.days,self.rooms,0)
        elif(a==3):
            rent=suiteroom.calculate(self.days,self.rooms,0)
        print("Name:",self.name)
        print("Address:",self.address)
        print("Mobile no:",self.mobile)
        print("No. of days:",self.days)
        print("No. of rooms:",self.rooms)
        print("room rent=",rent)
name=input("enter the name")
address=input("enter the address")
mobile=input("enter the mobile no")
days=int(input("enter the no of days"))
rooms=int(input("enter the no of rooms"))
print("1.Normal room","2.ACroom","3.Suite room",sep="\n")
a=int(input("enter the choice"))
m=Hotel(name,address,mobile,days,rooms,a)
m.display()
    
    
            
