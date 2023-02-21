import math
n=int(input())
c=0
if(n<=1):
    print("neither prime nor composite")
else:    
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            c=c+1
            break
    if(c==0):
        print("prime")
    else:
        print("not prime")
    
