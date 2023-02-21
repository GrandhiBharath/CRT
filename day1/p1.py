n=int(input())
p=n-1
q=2*n - 1
for i in range(1,n+1):
    for j in range(1,2*n):
        if(j<=p):
            print("*",end=" ")
        if(j>p and j<q):
            print("+",end=" ")
        if(j>=q):
            print("@",end=" ")
    p=p-1
    q=q-1
    print()
