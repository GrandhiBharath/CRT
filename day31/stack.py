n=int(input("enter the size"))
l=[0]*n
top=-1
def push(a,top,n,l):
    if(top!=n-1):
        top=top+1
        l[top]=a
    else:
        print("Stack overflow")
    return top
def pop(l,top):
    if(top==-1):
        print("Stack underflow")
    else:
        l.pop(top)
        top-=1
    return top
def display(l,top):
    if(top==-1):
        print("Stack is empty")
    else:
        while(top!=-1):
            print(l[top])
            top-=1
def peek(top,l):
    if(top==-1):
        print("empty stack")
    else:
        print("the peek element is ",l[top])
while(1):
    print("1.push","2.pop","3.display","4.peek",sep="\n")
    c=int(input("enter the choice"))
    if(c==1):
        a=int(input("enter the element"))
        top=push(a,top,n,l)
    elif(c==2):
        top=pop(l,top)
    elif(c==3):
        display(l,top)
    elif(c==4):
        peek(top,l)
    else:
        exit
    
    
    
