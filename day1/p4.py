n=int(input())
p=1
for i in range(1,2*n):
    a=5
    for j in range(1,n+1):
        if(j>=p):
            if(a==5):
                print("0",a,end="  ",sep="")
                a=a*2
            else:
                print(a,end="  ")
                a=a*2
        else:
            print(" ",end=" ")
    print()
    if(i<n):
        p=p+1
    else:
        p=p-1
