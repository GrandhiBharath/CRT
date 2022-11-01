l=list(map(int,input().split()))
for i in range(1,len(l)):
    for j in range(0,i+1):
        if(l[i]<l[j]):
            t=l[i]
            for k in range(i,j,-1):
                l[k]=l[k-1]
            l[j]=t
            break
        
print(l)
