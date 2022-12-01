class linkedlist:
    def __init__(self,value):
        self.flag=0
        self.value=value
        self.address=None
head=None
tail=None
def insert(head,tail,value):
    l=linkedlist(value)
    if(head==None):
        head=l
        tail=l
    else:
        tail.address=l
        tail=l
    return tail
def checkcir(p):
    if(p.address==None):
        print("not circular")
        return
    if(p.flag==0):
        p.flag=1
        p=p.address
        checkcir(p)
    else:
        print("circular list")
        return
def makecircular(tail):
    tail.address=head
    return tail
while(1):
    print("1.insert","2.check cir","3.make circular","4.exit",sep="\n")
    a=int(input("enter the choice"))
    if(a==1):
        value=int(input("enter the value "))
        tail=insert(head,tail,value)
        if(head==None):
            head=tail
    elif(a==2):
        checkcir(head)
    elif(a==3):
        tail=makecircular(tail)
    elif(a==4):
        break
    else:
        print("invalid choice")
        
    
