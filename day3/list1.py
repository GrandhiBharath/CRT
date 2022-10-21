l=list(map(int,input().split()))
for i in l:
    c1=0
    for j in l:
        if(i==j):
            c1=c1+1
    print(c1,end=" ")
print()
for i in range(0,len(l)):
    c2=0
    if(i==0):
        print("1",end=" ")
    else:
        for j in range(i,-1,-1):
            if(l[i]==l[j]):
                c2=c2+1
        print(c2,end=" ")
print()
for i in range(0,len(l)):
    c3=0
    for j in range(len(l)-1,i-1,-1):
        if(l[i]==l[j]):
            c3=c3+1
    print(c3,end=" ")

    
