n=int(input())
s=0
for i in range(1,n//2+1):
    if(n%i==0):
        s=s+i
if(s==n):
    print("perfect number")
if(s>n):
    print("abundant number")
if(s<n):
    print("deficient number")
