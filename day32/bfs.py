n=int(input("enter the number of nodes"))
m=[[0,1,1,0,0,0,0,0],[1,0,0,1,0,0,0,0],[1,0,0,1,1,0,0,0],[0,1,1,0,0,0,0,0],[0,0,1,0,0,1,1,1],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0]]
'''
for i in range(0,n):
    l1=list(map(int,input("enter the values").split()))
    l.append(l1)
print(len(m))
for i in m:
    print(len(i))'''
vis=[0]*n
l=[0]*n
s=0
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
r=enqueue(0,f,r,n,l)
f=0
c=0
while(c<n):
    if(vis[s]!=1):
        c=c+1
        print(s)
        vis[s]=1
        for i in range(0,n):
            if(m[s][i]==1 and vis[i]==0):
                r=enqueue(i,f,r,n,l)
                if(r==0 and f==-1):
                    f=0
        f=dequeue(f,r,l)
        if(f==-1):
            r=-1
        s=l[f]
    else:
        f=f+1
        if(f<n):
            s=l[f]

    
        
        
        
        
    
    
    
    

        
