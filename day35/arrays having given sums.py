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
for i in range(0,len(l)):
    a=i
    s=b
    if(m[a][s]>=1):
        while(s!=0 and a<len(l)):
            f=1
            if(a==0 and m[a][s]>=1):
                print(l[a],end=" ")
                s=s-l[a]
                f=0
            elif(a!=0 and m[a][s]!=m[a-1][s]):
                print(l[a],end=" ")
                s=s-l[a]
                f=0
            if(f!=0):
                a=a+1
            else:
                a=0
        print()
        
