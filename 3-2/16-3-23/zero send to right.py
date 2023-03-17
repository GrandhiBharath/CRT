'''l=list(map(int,input().split()))
a=len(l)
for i in range(a):
    if(l[i]==0):
        l.append(0)
        l.remove(l[i])
for i in l:
    print(i,end=" ") '''

l=list(map(int,input().split()))
a=len(l)
l1=[0]*a
c=0
for i in range(a):
    if(l[i]!=0):
        l1[c]=l[i]
        c=c+1
for j in l1:
    print(j,end=" ")

