class calci():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        print(self.x+self.y)
    def sub(self):
        print(self.x-self.y)
    def mul(self):
        print(self.x*self.y)
    def div(self):
        print(self.x//self.y)
class advcalci(calci):
    def __init__(self,m,n):       
        self.m=m
        self.n=n
        calci.__init__(self,m,n)  #super.__init__(a,b)
    def pow(self):
        print((self.m)**(self.n))
    def per(self):
        print(self.m%self.n)
a=advcalci(2,3)
a.add()
a.sub()
a.mul()
a.div()
a.pow()
a.per()
