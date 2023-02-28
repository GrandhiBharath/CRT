class user:
    def __init__(self,a):
        self.a=a
    def __add__(p,q):
        return p.a*q.a
    def __sub__(p,q):
        return 2*(p.a+q.a)
o1=user(10)
o2=user(20)
print(o1+o2)
print(o1-o2)
