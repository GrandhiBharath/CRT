l=list(map(int,input().split()))
s=int(input("enter the sum"))
m=[]
for i in range(0,len(l)):
    t=[0]*(s+1)
    m.append(t)
for j in range(0,len(l)):
    m[j][0]=1
for i in range(0,len(l)):
    for j in range(0,s+1):
        if(j<l[i]):
            m[i][j]=m[i-1][j]
        else:
            a=j-l[i]
            m[i][j]=m[i-1][a]+m[i-1][j]
for i in range(0,len(l)):
    for j in range(0,s+1):
        print(m[i][j],end=" ")
    print()
print(m[len(l)-1][s])

        
