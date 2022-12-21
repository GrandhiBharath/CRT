l=list(map(int,input().split()))
s=int(input("enter the sum"))
b=s
m=[]
for i in range(0,len(l)):
    t=[0]*(s+1)
    m.append(t)
for j in range(0,len(l)):
    m[j][0]=1
for i in range(0,len(l)):
    for j in range(1,s+1):
        if(i==0 and j>=l[i]):
            a=j-l[i]
            m[i][j]=m[i][a]
        else:
            if(j<l[i]):
                m[i][j]=m[i-1][j]
            else:
                a=j-l[i]
                m[i][j]=m[i-1][j]+m[i][a]
for i in range(0,len(l)):
    for j in range(0,s+1):
        print(m[i][j],end=" ")
    print()
print(m[len(l)-1][s])
