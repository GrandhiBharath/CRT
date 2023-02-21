n=int(input())
p=n
for i in range(1,2*n+1):
    for j in range(1,n+1):
        if(j<p):
            print(" ",end="")
        if(j>=p):
            print("* ",end="")
    if(i<n):
        p=p-1
    else:
        p=p+1
    print()
