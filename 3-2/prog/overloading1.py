class compute:
    def calculate(self,a,b,c=None):
        if(c==None):
            print("the modulus of the numbers:",a%b)
        else:
            print("the power of three numbers:",(a**b)**c)
o=compute()
a,b,c=map(int,input().split())
o.calculate(a,b)
o.calculate(a,b,c)
