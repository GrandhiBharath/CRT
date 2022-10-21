import math
l=list(map(int,input().split()))
c1=0
for i in l:
    if(i<=1):
        c1=c1
    else:
        c=0
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0):
                c=c+1
                break
        if(c==0):
            c1=c1+1
print(c1)
    
        
