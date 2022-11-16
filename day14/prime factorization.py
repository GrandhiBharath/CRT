n=int(input())
m=n
def prime(n):
    c=0
    for i in range(2,n//2+1):
        if(n%i==0):
            c=1
            break
    if(c==0):
        return true
def primefactors(n):
    for i in range(2,n):
        if(n%i==0):
            print(i,end=" ")
            n=n//i
            
if(prime(n)):
    print(n)
    
        
