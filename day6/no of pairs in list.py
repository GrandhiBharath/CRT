l=list(map(int,input().split()))
k=int(input())
l1=[0]*k
c=0
for i in range(0,len(l)):
    a=l[i]%k
    l1[a]=l1[a]+1
j=k-1
if(k%2==0):
    b=k//2
    c=c + (l1[b]*(l1[b]-1))//2
else:
    b=k//2+1
for i in range(0,b):
    if(i==0):
        if(l1[i]>0):
            c=c+((l1[i]*(l1[i]-1))//2)
    elif(i<j):
        if(l1[i]>0 and l1[j]>0):
            c=c+(l1[i]*l1[j])
        j=j-1
print(c)
                
                
                
            
            
        
        
    
