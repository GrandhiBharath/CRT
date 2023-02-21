n=int(input())
for i in range(1,n+1):
    a=i*2
    for j in range(1,n+1):
        if(a<10):
            a=str(a)
            a="0" + a
        print(a,end=" ")
        a=int(a)
        a=a*2
    print()

