n=int(input())
p=1
q=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<=p):
            print("*",end=" ")
        if(j>p and j<q):
            print("$",end=" ")
        if(j>=q):
            print("*",end=" ")
    if(i<(n+1)//2):
        p=p+1
        q=q-1
    else:
        p=p-1
        q=q+1
    print()
