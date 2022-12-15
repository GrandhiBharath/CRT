n=int(input("enter the size"))
l=[0]*n
f=-1
r=-1
def enqueue(a,f,r,n,l):
    if((r+1)%n==f):
        print("Queue is full")
        return r
    r=(r+1)%n
    l[r]=a
    return r
def dequeue(f,r,l):
    if(f==-1 and f==r):
        print("Queue underflow")
    elif(f==r):
        f=-1
    else:
         f=(f+1)%n
    return f
def display(f,n,r,l):
    if(f==-1):
        print("empty queue")
    else:
        if(f<=r):
            while(f<=r):
                print(l[f])
                f=f+1
        else:
            while(f<n):
                print(l[f])
                f=f+1
            f=0
            while(f<=r):
                print(l[f])
                f=f+1
while(1):
    print("1.enqueue","2.dequeue","3.display",sep="\n")
    c=int(input("enter the choice"))
    if(c==1):
        a=int(input("enter the element"))
        r=enqueue(a,f,r,n,l)
        if(r==0 and f==-1):
            f=0
    elif(c==2):
        f=dequeue(f,r,l)
        if(f==-1):
            r=-1
    elif(c==3):
        display(f,n,r,l)
    

  
