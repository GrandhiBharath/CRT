n=list(map(int,input().split()))
k=int(input())
l=0
f=0
h=len(n)-1
while(l<=h):
    mid=(l+h)//2
    if(n[mid]==k):
        f=1
        print(mid+1)
        break
    if(n[mid]<k):
        h=mid-1
    else:
        l=mid+1
if(f==0):
    print("element not found")
    
