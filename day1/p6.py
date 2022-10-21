n=int(input())
for i in range(1,n+1):
    for i in range(1,2*n):
        if(i==1 or i==2*n-1):
            for j in range(1,2*n):
                print("*",end=" ")
            print()
        else:
            for j in range(1,2*n):
                if(j==1 or j==2*n-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
