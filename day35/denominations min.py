l=list(map(int,input().split()))
s=int(input("enter the sum"))
m=[]
for i in range(0,len(l)):
    t=[99]*(s+1)
    m.append(t)
for i in range(0,len(l)):
    for j in range(0,s+1):
        if(l[i]==j):
            m[i][j]=1
        elif(l[i]<j):
            a=j-l[i]
            if(i==0):
                if(m[i][a]!=99):
                    m[i][j]=m[i][a]+1
            else:
                if(m[i][a]==99):
                    m[i][j]=m[i-1][j]
                else:
                    m[i][j]=min(m[i][a]+1,m[i-1][j])
for i in range(0,len(l)):
    for j in range(0,s+1):
        print(m[i][j],end="\t")
    print()
print(m[len(l)-1][s])
                    
            
