l=list(map(int,input().split()))
k=int(input())
i=j=m=s=0
while(j<len(l)):
    s=s+l[j]
    if((j-i+1)==k):
        if(s>m):
            m=s
        s=s-l[i]
        i=i+1
    j=j+1
print(m)
    

    
