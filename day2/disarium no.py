import math
n=int(input())
t=n
d=int(math.log(10,n))
i=1
s=0
while(n!=0):
    r=n//(10**d)
    s=s+(r**i)
    i=i+1
    if(n==0):
        break
    n=n%(10**d)
    d=d-1
if(s==t):
    print("disarium number")
else:
    print("no")
    
    
    
