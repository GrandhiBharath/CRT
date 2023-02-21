'''a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
def add(x):
    s=0
    for i in x:
        s=s+i
    return s
s1=add(a)
s2=add(b)
s3=add(c)
print(s1-s2)
print(s2-s3)'''



a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d={}
d1={}
for i in a:
    if(i not in d.keys()):
        d[i]=1
for i in b:
    if(i in d.keys()):
        d[i]-=1
    if(i not in d1.keys()):
        d1[i]=1
for i in c:
    if(i in d1.keys()):
        d1[i]-=1
for i in d.keys():
    if(d[i]!=0):
        print(i)
for i in d1.keys():
    if(d1[i]!=0):
        print(i)





