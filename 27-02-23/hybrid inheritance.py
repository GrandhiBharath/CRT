class A:
    def display(self):
        print("i am in class A")
class B(A):
    def display(self):
        print("i am in class B")
        super().display()
class C(B):
    def display(self):
        print("i am in class C")
        super().display()
class D(C,A):
    def display(self):
        print("i am in class D")
        super().display()
p=D()
p.display()
