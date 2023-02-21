l=list(map(int,input().split()))
l1=[0]*(max(l)-min(l)+1)
a=min(l)
for i in l:
    l1[i-a]+=1
for i in range(1,len(l1)):
    l1[i]=l1[i-1]+l1[i]
l2=[0]*len(l)
for i in l:
    b=l1[i-a]
    l2[b]=i
    l1[i-a]-=1
print(l2)

    
