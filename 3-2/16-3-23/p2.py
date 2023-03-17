n=int(input())
p=n
for i in range(1,n+1):
    for j in range(1,p+1):
        if((i%2!=0 and j%2!=0) or (i%2==0 and j%2==0)):
            print("0",end=" ")
        if((i%2!=0 and j%2==0) or (i%2==0 and j%2!=0)):
            print("1",end=" ")
    p=p-1
    print()
