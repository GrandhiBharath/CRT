a,b=map(int,input().split())
s2=0
for i in range(a,b+1):
    l=[]
    s=str(i)
    s1=0
    for j in s:
        l.append(int(j))
        s1=s1+int(j)
    if(max(l)==(s1-max(l))):
        s2=s2+i
print(s2)
    
