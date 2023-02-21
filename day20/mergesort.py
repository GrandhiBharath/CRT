l=list(map(int,input().split()))
i=0
j=len(l)
def merge(l,i,m,j):
    r=[]
    l1=l[i:m+1]
    l2=l[m+1:j+1]
    p,q=0,0
    while(p<len(l1) and q<len(l2)):
        if(l1[p]<l2[q]):
            r.append(l1[p])
            p+=1
        else:
            r.append(l2[q])
            q+=1
    if(p==len(l1)):
        while(q<len(l2)):
            r.append(l2[q])
            q+=1
    if(q==len(l2)):
        while(p<len(l1)):
            r.append(l1[p])
            p+=1
    return r
def mergesort(l,i,j):
    if(i==j):
        return
    else:
        m=(i+j)//2
        mergesort(l,i,m)
        mergesort(l,m+1,j)
        l[i:j+1]=merge(l,i,m,j)
        return l
v=mergesort(l,i,j)
print(v)

    
