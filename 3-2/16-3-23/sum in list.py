l=list(map(int,input().split()))
a=int(input())
for i in range(len(l)):
    for j in range(i,len(l)):
        if((l[i]+l[j])==a):
            print(i,j,end=" ")
            break
