class Basic:
    def __init__(self):
        self.basic=10000
class CSE(Basic):
    def __init__(self,bonus):
        super().__init__()
        self.bonus=bonus
        self.penalty=0.1
    def display(self):
        s=self.basic+self.bonus
        total=s-s*self.penalty
        print("total salary:",total)
class ECE(Basic):
     def __init__(self,bonus):
        super().__init__()
        self.bonus=bonus
        self.penalty=0.05
     def display(self):
        s=self.basic+self.bonus
        total=s-s*self.penalty
        print("total salary:",total)
class IT(Basic):
     def __init__(self,bonus):
        super().__init__() 
        self.bonus=bonus
        self.penalty=0.15
     def display(self):
        s=self.basic+self.bonus
        total=s-s*self.penalty
        print("total salary:",total)
class DS(Basic):
     def __init__(self,bonus):
        super().__init__() 
        self.bonus=bonus
        self.penalty=0.2
     def display(self):
        s=self.basic+self.bonus
        total=s-s*self.penalty
        print("total salary:",total)
class AIML(Basic):
     def __init__(self,bonus):
        super().__init__() 
        self.bonus=bonus
        self.penalty=0.01
     def display(self):
        s=self.basic+self.bonus
        total=s-s*self.penalty
        print("total salary:",total)
print("1.CSE","2.ECE","3.IT","4.DS","5.AIML",sep="\n")
n=int(input("enter the choice"))
bonus=int(input("enter the bonus"))
if(n==1):
    a=CSE(bonus)
elif(n==2):
    a=ECE(bonus)
elif(n==3):
    a=IT(bonus)
elif(n==4):
    a=DS(bonus)
elif(n==5):
    a=AIML(bonus)
a.display()
    
    
