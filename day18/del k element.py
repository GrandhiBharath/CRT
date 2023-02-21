def delete(l,k,i):
    if(i==-1):
        return l
    if(l[i]==k):
        l.pop(i)
        return
    else:
        i-=1
        delete(l,k,i)
        return l
l=list(map(int,input().split()))
k=int(input())
i=len(l)-1
v=delete(l,k,i)
print(v)
