l=list(map(int,input().split()))
l1=[0]*(max(l)-min(l)+1)
l2=[0]*len(l)
a=min(l)
for i in l:
    l1[i-a]+=1
for j in range(1,len(l1)):
    l1[j]=l1[j]+l1[j-1]
for k in l:
    l2[l1[k-a]-1]=k
    l1[k-a]-=1
print(l2)
