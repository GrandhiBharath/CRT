class polygon:
    def area(self,s):
        self.s=s
        print("area of square:",self.s*self.s)
    def area(self,l,b):
        self.l=l
        self.b=b
        print("area of rectangle:",self.l*self.b)
o=polygon() 
#o.area(4)   cant be called because in python method overloading is not possible
o.area(2,4)
