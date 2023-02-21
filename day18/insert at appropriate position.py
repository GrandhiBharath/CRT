def insert(l,k):
    if(len(l)==0 or l[-1]<k):
        l.append(k)
        return
    else:
        t=l.pop(-1)
        insert(l,k)
        l.append(t)
        return 
l=list(map(int,input().split()))
k=int(input())
insert(l,k)
print(l)
