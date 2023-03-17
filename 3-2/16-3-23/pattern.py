n=int(input())
p,q=n,n
for i in range(1,n+1):
    for j in range(1,2*n):
        if(j<p or j>q):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    p=p-1
    q=q+1
    print()
