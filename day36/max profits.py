n=int(input())
l=list(map(int,input("enter the profits").split()))
m=[]
for i in range(n):
    t=[0]*(n+1)
    m.append(t)
for i in range(n):
    for j in range(1,n+1):
        if(i==0):
            m[i][j]=l[i]*j
        else:
            if((i+1)>j):
                m[i][j]=m[i-1][j]
            else:
                a=j-(i+1)
                m[i][j]=max(l[i]+m[i][a],m[i-1][j])
for i in range(n):
    for j in range(n+1):
        print(m[i][j],end=" ")
    print()
print("Maximum profit: ",m[n-1][n])
s=m[n-1][n]
i=n-1
j=n
while(s!=0):
    if(i==0):
        print(l[i],end=" ")
        s=s-l[i]
        a=j-(i+1)
        j=a
        i=n-1
    elif(m[i][j]==m[i-1][j]):
        i=i-1
    else:
        print(l[i],end=" ")
        s=s-l[i]
        a=j-(i+1)
        j=a
        i=n-1
    
                
