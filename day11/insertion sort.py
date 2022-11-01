l=list(map(int,input().split()))
for k in range(1,len(l)):
    j=k-1
    a=l[k]
    while(j>=0):
        if(a<l[j]):
            l[j+1]=l[j]
        else:
            l[j+1]=a
            break
        j-=1
    if(j==-1):
        l[j+1]=a
print(l)
            
    
