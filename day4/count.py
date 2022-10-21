l=list(map(int,input().split()))
a=[0]*(max(l)+1)
b=[0]*(abs(min(l)))
for i in l:
    if(i>=0):
        a[i]=a[i]+1
    else:
        b[i]=b[i]+1    
for k in range(len(b),0,-1):
    if(b[-k]>0):
        print("-",k,"->",b[-k],sep="")
for j in range(0,len(a)):
    if(a[j]>0):
        print(j,"->",a[j],sep="")

    
 
