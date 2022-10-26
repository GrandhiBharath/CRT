l=list(map(int,input().split()))
s1=0
c=0
for i in range(0,len(l)-1):
    s1=s1+l[i]
    s2=0
    for j in range(len(l)-1,i,-1):
        s2=s2+l[j]
        if(s1==s2):
            if((i+1)==(j-1)):
                c=1
                print(i+2)
if(c==0):
    print("-1")
    
        
        
