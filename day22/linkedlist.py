class linkedlist:
    def __init__(self,value):
        self.value=value
        self.address=None
head=None
tail=None
def insertfirst(head,value):
    l=linkedlist(value)
    if(head==None):
        head=l
        tail=l
    else:
        l.address=head
        head=l
    return head
def insert(head,tail,value):
    l=linkedlist(value)
    if(head==None):
        p=None
        head=l
        tail=l
    else:
        p=tail.address
        tail.address=l
        tail=l
    return tail
def display(head):
    p=head
    if(p==None):
        print("LinkedList is empty")
        return
    else:
        print(p.value)
        p=p.address
        if(p!=None):
            display(p)
def removefirst(head):
    if(head==None):
        print("Empty list")
        return
    else:
        head=head.address
    return head
while(1):
    print('1.insertfirst','2.insert','3.display','4.removefirst','5.removelast','6.exit',sep="\t")
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
    elif(c==5):
        
    elif(c==6):
        break
    else:
        print("Invalid choice")
        break
    







        
        
