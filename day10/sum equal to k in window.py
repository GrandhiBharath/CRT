l=list(map(int,input().split()))
k=int(input())
i,j,s,m=0,0,0,0
while(j<len(l)):
    s=s+l[j]
    if(s==k):
        if(m<(j-i+1)):
            m=j-i+1
        s=s-l[i]
        i+=1
    j+=1
print(m)
           
