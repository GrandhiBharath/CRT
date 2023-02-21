class college:
    cname='vits' #class variable
    def __init__(self,rno,branch):
        self.rollno=rno  #instance variable
        self.branch=branch
    def display(self):
        print(self.rollno)
        print(self.branch)
        print(college.cname)   #inside class to access we use class name
c=college(1,'aiml')
print(c)
c1=college(2,'ds')
print(c1)
c.display()
c1.display()
print(c.cname,c1.cname)
c.cname="vignan"           #changing using object...changes that particular object
print(c.cname,c1.cname)
college.cname="vignan"     #changing using class name...changes all objects
print(c.cname,c1.cname)

