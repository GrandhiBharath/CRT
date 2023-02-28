class RBI:
    def __init__(self,r):
        self.r=r
    def Interest(self):
        ci=100*((1 + self.r/100)**4.5)
        return ci
class SBI(RBI):
    def Interest(self):
        ci1=super().Interest()
        print("SBI compund interest:",ci1)
        si=(100*4.5*self.r)/100 + 100
        print("SBI simple interst:",si)
class IndianBank(RBI):
    def Interest(self):
        ci2=super().Interest()
        print("IndianBank compund interest:",ci2)
        si=(100*4.5*self.r)/100 + 100
        print("SBI simple interst:",si)
class CanaraBank(RBI):
    def Interest(self):
        ci3=super().Interest()
        print("CanaraBank compund interest:",ci3)
        si=(100*4.5*self.r)/100 + 100
        print("SBI simple interst:",si)
a=eval(input("enter the rate of SBI"))
b=eval(input("enter the rate of IndianBank"))
c=eval(input("enter the rate of CanaraBank"))
o1=SBI(a)
o2=IndianBank(b)
o3=CanaraBank(c)
o1.Interest()
o2.Interest()
o3.Interest()


