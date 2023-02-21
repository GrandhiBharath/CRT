'''import math
n=int(input())
for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0):
        a=n//i
        if((i+1)==a):
            print("pronic number")
else:
    print("no")'''

import math
n=int(input())
a=int(math.sqrt(n))
if((a*(a+1))==n):
    print("pronic number")
else:
    print("no")
    
