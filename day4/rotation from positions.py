l=list(map(int,input().split()))
n=int(input())
p,q=map(int,input().split())
n=n%((q-p)+1)
while(n!=0):
    t=l[q]
    for i in range(q-1,p-1,-1):
        l[i+1]=l[i]
    l[p]=t
    n=n-1
print(l)
