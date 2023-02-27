class unit:
    def calculate(marks):
        if(marks>=36):
            return "pass"
        else:
            return "fail"
class mid:
    def calculate(marks):
        if(marks>=20):
            return "pass"
        else:
            return "fail"
class student(unit,mid):
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self,a):
        print(self.name)
        if(a==1):
            m=unit.calculate(self.marks)
            print(m)
        if(a==2):
            m=mid.calculate(self.marks)
            print(m)
o=student("bharath",45)
o.display(1)
        
