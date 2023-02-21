import math
n=int(input())
def factors(n):
    i=9
    c=""
    while(n>1):
        if(n%i==0):
            if(i==1):
                c="Invalid"
                break
            else:
                c=c+str(i)
                n=n//i
                i=9
        else:
            i-=1
    
    return c
if(n<10):
    print('1',n,sep="")
else:
    if(factors(n)=="Invalid"):
        print("Invalid")
    else:
        v=int(factors(n))
        s=0
        while(v>1):
            r=v%10
            s=s*10+r
            v=v//10
        print(s)
            
            
