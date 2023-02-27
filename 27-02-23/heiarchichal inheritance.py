class Bank:
    def __init__(self,a):
        self.a=a
    def display(self):
        print("initial amount",self.a)
class SBI(Bank):
    def __init__(self,a,s):
        super().__init__(a)
        self.s=s
    def display(self):
        super().display()
        print("amount in SBI bank:",self.a+self.s)
class HDFC(Bank):
    def __init__(self,a,h):
        super().__init__(a)
        self.h=h
    def display(self):
        super().display()
        print("amount in HDFC bank:",self.a+self.h)
s=SBI(1000,200)
h=HDFC(1000,300)
s.display()
h.display()
