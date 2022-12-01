class linkedlist:
    def __init__(self,value):
        self.value=value
        self.address=None
head=None
tail=None
head1=None
tail1=None
head2=None
tail2=None
def insert(head,tail,value):
    l=linkedlist(value)
    if(head==None):
        head=l
        tail=l
    else:
        tail.address=l
        tail=l
    return tail
def display(head):
    p=head
    if(p==None):
        print("\nLinkedList is empty\n")
        return
    else:
        print(p.value)
        p=p.address
        if(p!=None):
            display(p)
def reverselist(head,tail):
    p=head
    q=tail
    if(head==None and tail==None):
        print("\nlinked list is empty\n")
        return
    if(p==q):
        return
    t=p.address
    t1=t.address
    while(t!=None):
        if(p==head):
            p.address=None
            t.address=p
            p=t
            t=t1
        else:
            t1=t.address
            t.address=p
            p=t
            t=t1
    head=p
    return head
def addinglist(p,q,qu,head2,tail2):
    while(p!=None and q!=None):
        a=p.value + q.value + qu
        qu=a//10
        r=a%10
        tail2=insert(head2,tail2,r)
        if(head2==None):
            head2=tail2
        p=p.address
        q=q.address
    if(p==None and q!=None):
        b=q.value+qu
        while(b!=0):
            r=b%10
            tail2=insert(head2,tail2,r)
            b=b//10
    elif(p!=None and q==None):
        b=p.value+qu
        while(b!=0):
            r=b%10
            tail2=insert(head2,tail2,r)
            b=b//10
    elif(qu<10):
        tail2=insert(head2,tail2,qu)
    else:
        while(qu!=0):
            r=qu%10
            tail2=insert(head2,tail2,r)
            qu=qu//10
    return head2,tail2
while(1):
    a=int(input("\nenter the list number \n"))
    if(a==1):
        print('1.insert','2.display',sep="\n")
        print('3.reverselist','4.exit',sep="\n")
        c=int(input("choose your choice "))
        if(c==1):
            value=int(input("enter the value "))
            tail=insert(head,tail,value)
            if(head==None):
                head=tail
        elif(c==2):
            display(head)
        elif(c==3):
            k=head
            head=reverselist(head,tail)
            tail=k
        elif(c==4):
            break
        else:
            print("Invalid choice")
            break
    elif(a==2):
        print('1.insert','2.display',sep="\n")
        print('3.reverselist','4.exit',sep="\n")
        c=int(input("choose your choice "))
        if(c==1):
            value=int(input("enter the value "))
            tail1=insert(head1,tail1,value)
            if(head1==None):
                head1=tail1
        elif(c==2):
            display(head1)
        elif(c==3):
            k=head1
            head1=reverselist(head1,tail1)
            tail1=k
        elif(c==4):
            break
        else:
            print("Invalid choice")
            break
    elif(a==3):
        l=addinglist(head,head1,0,head2,tail2)
        l=list(l)
        head2=l[0]
        tail2=l[1]
    elif(a==4):
        k=head2
        head2=reverselist(head2,tail2)
        tail2=k
        display(head2)
    
    







        
        
