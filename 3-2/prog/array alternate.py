import math
l=list(map(int,input().split()))
pl=[]
cl=[]
def prime(n):
    c=0
    if(n==1):
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            c=1
            break
    if(c==0):
        return 1
    else:
        return 0
p,c=0,0
for i in l:
    if(prime(i)):
        p=p+1
        pl.append(i)
    else:
        c=c+1
        cl.append(i)
pl.sort()
cl.sort()
s=0
if(p<c):
    for i in range(0,len(cl)-p-1):
        s=s+cl[i]
else:
    for i in range(0,len(pl)-c-1):
        s=s+pl[i]
print(s)
    
    
