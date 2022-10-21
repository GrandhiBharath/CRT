import math
l=list(map(int,input().split()))
l1=[]
n=1
b=2
while(n<=max(l)+):
    c=0
    for j in range(2,int(math.sqrt(b))+1):
        if(b%j==0):
            c=c+1
            break
    if(c==0):
        l1.append(b)
        n=n+1
    b=b+1
for i in l:
    print(l1[i-1],end=" ")
