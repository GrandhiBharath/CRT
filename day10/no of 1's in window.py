l=list(map(int,input().split()))
k=int(input())
i,j=0,0
m,c=0,0
f,la=0,0
while(j<len(l)):
    if(l[j]==1):
        c=c+1
    if((j-i+1)==k):
        if(c>m):
            f=i
            la=j
            m=c
        if(l[i]==1):
            c=c-1
        i+=1
    j+=1
print(m)
print(f,la,sep=" ")

    
        
