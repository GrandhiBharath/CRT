a=list(map(int,input().split()))
def heapify(a,n,s):
    l=s
    left=s*2+1
    right=s*2+2
    if(left<n):
        if(a[left]>a[l]):
            l=left
    if(right<n):
        if(a[right]>a[l]):
            l=right
    if(l!=s):
        a[l],a[s]=a[s],a[l]
        heapify(a,n,l)
def heapsort(a,n,s):
    for i in range(s,-1,-1):
        heapify(a,n,i)
    for j in range(n-1,0,-1):
        a[j],a[0]=a[0],a[j]
        heapify(a,j,0)
n=len(a)
heapsort(a,n,n//2-1)
print(a)


        
