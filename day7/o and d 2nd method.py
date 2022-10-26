n=list(map(int,input().split()))
k=int(input())
l=0
r=len(n)-1
a,b=0,0
d1,d2=0,0
while(l<=r):
    if(n[l]==k):
        if(a==0):
            a=1
            d1=l
    l=l+1
    if(n[r]==k):
        if(b==0):
            b=1
            d2=r
    r=r-1
    if(d1!=0 and d2!=0):
        break
if(a==0):
    print("-1")
else:
    print(d2-d1)
        
        
