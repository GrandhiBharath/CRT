import math
n=int(input())
def prime(n):
    c=0
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            c=1
            break
    if(c==0):
        return 1
    else:
        return 0
while(n!=1):
    if(prime(n)):
        print(n)
        break
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                print(i,end=" ")
                n=n//i
                break

    
        
