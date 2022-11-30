class doublelinkedlist:
    def __init__(self,value):
        self.prevaddress=None
        self.value=value
        self.nextaddress=None
head=None
tail=None
def insertfirst(head,value):
    l=doublelinkedlist(value)
    if(head==None):
        head=l
        tail=l
    else:
        l.nextaddress=head
        head.prevaddress=l
        head=l
    return head
def insert(head,tail,value):
    l=doublelinkedlist(value)
    if(head==None):
        head=l
        tail=l
    else:
        tail.nextaddress=l
        l.prevaddress=tail
        tail=l
    return tail
def display(p):
    if(p==None):
        print("\ndoubleLinkedList is empty\n")
        return
    else:
        print(p.value)
        if(p==tail):
            k=tail
        p=p.nextaddress
        if(p!=None):
            display(p)
        else:
            print()
            while(k!=None):
                print(k.value)
                k=k.prevaddress
def removefirst(head):
    p=head
    if(p==None):
        print("\nEmpty list\n")
        return
    else:
        head=p.nextaddress
        p.nextaddress=None
        del p
    return head
def removelast(q,tail):
    if(q==tail):
        del q
        tail=None
    elif(q.nextaddress==tail):
        q.nextaddress=None
        del tail
        tail= q
    else:
        q=q.nextaddress
        if(q!=None):
            tail=removelast(q,tail)
    return tail
def insertafter(k,value,head,tail):
    l=doublelinkedlist(value)
    p=head
    c=1
    if(p==None):
        head=l
        tail=l
    else:
        while(c<k):
            if(p!=None):
                p=p.nextaddress
                c+=1
            else:
                print("\ninvalid pos\n")
                return tail
        a=p.nextaddress
        p.nextaddress=l
        l.prevaddress=p
        l.nextaddress=a
        a.prevaddress=l
    return tail
def insertbefore(k,value,head,tail):
    l=doublelinkedlist(value)
    p=head
    c=1
    if(p==None):
        head=l
        tail=l
    else:
        while(c<k-1):
            if(p!=None):
                p=p.address
                c+=1
            else:
                print("\ninvalid pos\n")
                return tail
        a=p.nextaddress
        p.nextaddress=l
        l.prevaddress=p
        l.nextaddress=a
        a.prevaddress=l
    return tail
def delspecpos(k):
    p=head
    while(k-1):
        t=p
        if(p!=None):
            p=p.nextaddress
            k-=1
        else:
            print("\ninvalid pos\n")
            return
    t.nextaddress=p.nextaddress
    a=p.nextaddress
    a.prevaddress=t
    p.nextaddress=None
    del(p)
def reversedisplay(head):
    p=head
    if(p==None):
        print("\ndoubleLinkedList is empty\n")
        return
    else:
        t=p.value
        a=p
        p=p.nextaddress
        if(p!=None):
            reversedisplay(p)
            print(t)
        else:
            print(t)
            return
def reverselist(head,tail):
    p=head
    q=tail
    if(head==None and tail==None):
        print("\ndoublelinked list is empty\n")
        return
    if(p==q):
        return
    t=p.nextaddress
    t1=t.nextaddress
    while(t!=None):
        if(p==head):
            p.nextaddress=None
            t.nextaddress=p
            p=t
            t=t1
        else:
            t1=t.nextaddress
            t.nextaddress=p
            p=t
            t=t1
    head=p
    return head
def count(k,p,q):
    if(p==None):
        return 0
    if(p==q):
        return 1
    while(p!=q):
        k=k+1
        p=p.nextaddress
    return k+1
def midelements(k,p):
    c=1
    if(k==0):
        print("\ndoublelinkedlist is empty\n")
        return
    if(k%2==0):
        n=k//2+1
        while(c<=n):
            if(c==k//2 or c==n):
                print(p.value)
            p=p.nextaddress
            c=c+1
    else:
        while(c<=k//2):
            p=p.nextaddress
            c=c+1
        print(p.value)
    return
while(1):
    print('1.insert first','2.insert','3.display','4.remove first','5.remove last','6.insert after','7.insert before',sep="\n")
    print('8.del specific pos','9.reverse display','10.reverselist','11.count','12.mid elements','13.exit',sep="\n")
    c=int(input("choose your choice "))
    if(c==1):
        value=int(input("enter the value "))
        head=insertfirst(head,value)
        if(tail==None):
            tail=head
    elif(c==2):
        value=int(input("enter the value "))
        tail=insert(head,tail,value)
        if(head==None):
            head=tail
    elif(c==3):
        display(head)
    elif(c==4):
        head=removefirst(head)
        if(head==None):
            tail=None
    elif(c==5):
        tail=removelast(head,tail)
        if(tail==None):
            head=None
    elif(c==6):
        value=int(input("enter the value "))
        k=int(input("enter the position "))
        tail=insertafter(k,value,head,tail)
        if(head==None):
            head=tail
    elif(c==7):
        value=int(input("enter the value"))
        k=int(input("enter the position"))
        if(k==1):
            head=insertfirst(head,value)
            if(tail==None):
                tail=head
        else:
            tail=insertbefore(k,value,head,tail)
            if(head==None):
                head=tail
    elif(c==8):
        k=int(input("enter the pos"))
        if(k==1):
            head=removefirst(head)
            if(head==None):
                tail=None
        else:
            delspecpos(k)
    elif(c==9):
        reversedisplay(head)
    elif(c==10):
        k=head
        head=reverselist(head,tail)
        tail=k
    elif(c==11):
        k=count(0,head,tail)
        print(k)
    elif(c==12):
        k=count(0,head,tail)
        midelements(k,head)
    elif(c==13):
        break
    else:
        print("Invalid choice")
        break
