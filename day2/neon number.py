n=int(input())
t=n
a=n*n
s=0
while(a!=0):
    r=a%10
    s=s+r
    a=a//10
if(s==t):
    print("neon number")
else:
    print("not a neon number")
    
    
    
