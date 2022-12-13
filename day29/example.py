class calci():
    m=56
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
a=calci(10,20)
b=calci(30,49)
a.add()
a.mul()
b.sub()
b.div()
a.m=89
print(a.m,b.m)
