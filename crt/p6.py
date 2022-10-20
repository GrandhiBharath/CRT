n=int(input())
p=n
q=n+1
for i in range(1,n+n+1):
    for j in range(1,n+n+1):
        if(j<=p):
            print("*",end='')
        elif(j>p and j<q):
            print(" ",end='')
        else:
            print("*",end='')
    if(i<n):
        p=p-1
        q=q+1
    if(i>=n+1):
        p=p+1
        q=q-1
    print()
        
