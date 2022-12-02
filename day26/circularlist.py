class circularlist:
    def __init__(self,value):
        self.value=value
        self.address=None
tail=None
def insert(tail,value):
    l=circularlist(value)
    p=tail
    if(tail==None):
        tail=l
        tail.address=tail
    else:
        a=tail.address
        tail.address=l
        tail=l
        tail.address=a
    return tail
def insertfirst(tail,value):
    l=circularlist(value)
    p=tail
    if(tail==None):
        tail=l
        tail.address=tail
    else:
        a=tail.address
        l.address=a
        tail.address=l
    return tail
def display(tail):    
    if(tail==None):
        print("\nempty list\n")
        return
    a=tail.address
    while(a!=tail):
        print(a.value)
        a=a.address
    print(a.value)
    return
def insertspecpos(k,value,tail):
    l=circularlist(value)
    c=1
    p=tail
    if(p==None):
        tail=l
    else:
        p=tail.address
        while(c<k-1):
            if(p!=None):
                p=p.address
                c+=1
            else:
                print("\ninvalid pos\n")
                return tail
        a=p.address
        p.address=l
        l.address=a
    return tail
def dellast(tail):
    a=tail
    p=tail.address
    while(p.address!=tail):
        p=p.address
    p.address=tail.address
    del(tail)
    tail=p
    return tail
def delfirst(tail):
    p=tail.address
    a=p.address
    del(p)
    tail.address=a
    return tail
def delspecpos(k,tail):
    p=tail.address
    while(k-1):
        t=p
        if(p.address!=tail.address):
            p=p.address
            k=k-1
        else:
            print("\ninvalid pos\n")
            return
    t.address=p.address
    if(p==tail):
        tail=t
    p.address=None
    del(p)
    return tail
while(1):
    print("1.insert","2.insertfirst","3.display","4.insert spec pos","5.del last","6.del first","7.del spec pos","8.exit",sep="\n")
    c=int(input("choose your choice"))
    if(c==1):
        value=int(input("enter the value "))
        tail=insert(tail,value)
    elif(c==2):
        value=int(input("enter the value "))
        tail=insertfirst(tail,value)
    elif(c==3):
        display(tail)
    elif(c==4):
        value=int(input("enter the value"))
        k=int(input("enter the position"))
        if(k==1):
            tail=insertfirst(tail,value)
        else:
            tail=insertspecpos(k,value,tail)
    elif(c==5):
        tail=dellast(tail)
    elif(c==6):
        tail=delfirst(tail)
    elif(c==7):
        k=int(input("enter the pos"))
        if(k==1):
            tail=delfirst(tail)
        else:
            tail=delspecpos(k,tail)
    elif(c==8):
        break
    else:
        print("\ninvalid choice\n")
        break
        

        
