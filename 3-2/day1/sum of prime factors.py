import math
n=int(input())
s=0
def prime(n):
    c=1
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            c=0
            break
    return c
if(prime(n)):
    print(n)
else:
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            if(prime(i)):
                s=s+i
            if(prime(n//i)):
                s=s+(n//i)
    print(s)
        
