def insert(l,k):
    if(len(l)==0 or l[-1]<k):
        l.append(k)
        return
    else:
        t=l.pop(-1)
        insert(l,k)
        l.append(t)
        return
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in l2:
    insert(l1,i)
print(l1)
