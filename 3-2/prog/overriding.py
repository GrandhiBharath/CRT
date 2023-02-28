class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self,a,b):
        print("area of rectangle: ",self.a*self.b)
class Square(Rectangle):
    def __init__(self,a,b,s):
        super().__init__(a,b)
        self.s=s
    def area(self,a,b):
        print("area of square: ",self.s*self.s)
        super().area(a,b)
a=int(input("enter the length of rect"))
b=int(input("enter the breadth of rect"))
s=int(input("enter the side of square"))
o1=Rectangle(a,b)
o2=Square(a,b,s)
o1.area(a,b)
o2.area(a,b)
