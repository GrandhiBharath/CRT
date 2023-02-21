def insert(l,k):
    if(len(l)==0 or l[-1]<k):
        l.append(k)
        return
    else:
        t=l.pop(-1)
        insert(l,k)
        l.append(t)
        return
def sort(l):
    if(len(l)==1):
        return
    else:
        x=l.pop(-1)
        sort(l)
        insert(l,x)
        return
l=list(map(int,input().split()))
sort(l)
print(l)

