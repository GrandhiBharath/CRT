class vignan:
    def __init__(self,a):
        self.a=a
    def __add__(p,q):
        return p.a-q.a
o1=vignan(10)
o2=vignan(20)
print(o1+o2) #a+b----> a.__add__(b)
