n=int(input())
l=list(map(int,input().split()))
i=0
while(i<n):
    if(l[i]%10==0):
       l.append(l[i])
       l.remove(l[i])
       n-=1
    else:
        i+=1
print(l)

