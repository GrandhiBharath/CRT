l=list(map(int,input().split()))
l1=[0]*(max(l)-min(l)+1)
a=min(l)
for i in l:
    l1[i-a]=l1[i-a]+1
k=0
for j in range(0,len(l1)):
    while(l1[j]>0):
        l[k]=j+a
        k+=1
        l1[j]-=1
print(l)

        
