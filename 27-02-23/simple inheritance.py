class A:
    def __init__(self,a):
        self.a=a
    def display(self):
        print("value in parent class",self.a)
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
    def display(self):
        print("value in child class",self.b)
        super().display()
o1=A(10)
o2=B(10,20)
o1.display()
o2.display()
