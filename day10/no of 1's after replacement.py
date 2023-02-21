l=list(map(int,input().split()))
k=int(input())
m=0
r=0
i,j=0,0
while(j<len(l)):
    if(l[j]==0):
        if(r<k):
            r=r+1
        else:
            if(m<(j-i)):
                m=j-i
            if(l[i]==0):
                r-=1
            i+=1
            j-=1
    else:
        if(r>=k):
            if(m<(j-i)):
                m=j-i+1
    j+=1
if(m==0):
    print(len(l))
else:
    print(m)
    
    
    
    
    
    
