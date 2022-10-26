l=list(map(int,input().split()))
k=int(input())
c,d,m=0,0,0
for i in range(0,len(l)):
    if(k==l[i]):
        c=1
        d=i+1
        print(i+1,end=" ")
        if(m==0):
            m=1
            a=i+1
if(c==0):
    print("-1","-1",sep="\n")
else:
    print()
    print(d-a)
