l=list(map(int,input().split()))
for i in range(0,len(l)):
    m=i
    for j in range(i+1,len(l)):
        if(l[j]<l[m]):
            m=j
    t=l[i]
    l[i]=l[m]
    l[m]=t
print(l)
        
        
        
