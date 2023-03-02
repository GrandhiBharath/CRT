n=int(input())
l=list(map(int,input().split()))
l1=sorted(l)
d={}
c=0
for i in range(0,len(l1),2):
    d[l1[i]]=l1[(n-i)-1]
    d[l1[(n-i)-1]]=l1[i]
for i in range(0,len(l),2):
    if(l[i+1]!=d[l[i]]):
        c=c+1
if(c==0):
    print(c)
else:
    print(c-1)
for i in range(0,len(l),2):
    if(l[i+1]!=d[l[i]]):
        a=l.index(d[l[i]])
        l[i+1],l[a]=l[a],l[i+1]
print(l)
