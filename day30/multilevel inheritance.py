class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name of the person:",self.name)
class staff(person):
    def __init__(self,name,ID):
        person.__init__(self,name)
        self.ID=ID
    def display(self):
        person.display(self)
        print("Staff ID:",self.ID)
class tempstaff(staff):
    def __init__(self,name,ID,days,hrs):
        staff.__init__(self,name,ID)
        self.days=days
        self.hrs=hrs
        self.salary=0
    def display(self):
        staff.display(self)       #if called with super(),no need of self
        print("No. of days:",self.days)
        print("No. of hrs worked",self.hrs)
        self.salary=self.days*self.hrs*150
        print("Total Salary",self.salary)
name=input("enter the name")
ID=int(input("enter the id"))
days=int(input("enter the days"))
hrs=int(input("enter the hrs worked"))
a=tempstaff(name,ID,days,hrs)
a.display()
        
