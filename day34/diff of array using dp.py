l=list(map(int,input().split()))
s=sum(l)
d=int(input("enter the difference"))
m=[]
s=(s+d)//2
for i in range(0,len(l)):
    t=[0]*(s+1)
    m.append(t)
for j in range(0,len(l)):
    m[j][0]=1
for i in range(0,len(l)):
    for j in range(0,s+1):
        if(j<l[i]):
            m[i][j]=m[i-1][j]
        elif(j==l[i]):
            m[i][j]=1
        else:
            a=j-l[i]
            m[i][j]=max(m[i-1][a],m[i-1][j])
if(m[len(l)-1][s]==1):
    print("TRUE")
else:
    print("FALSE")


