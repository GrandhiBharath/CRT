import math
n=int(input())
l=[]
for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        if(i==n//i):
            l.append(i)
        else:
            l.extend([i,n//i])


        
    
