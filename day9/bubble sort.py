l=list(map(int,input().split()))
for i in range(0,len(l)-1):
    c=0
    for j in range(0,len(l)-i-1):
        if(l[j]>l[j+1]):
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
            c=1
    if(c==0):
        break
print(l)
