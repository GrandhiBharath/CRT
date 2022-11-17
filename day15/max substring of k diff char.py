s=input()
k=int(input())
i,j=0,0
d={}
c,m=0,0
while(j<len(s)):
    if(len(d)<=k):
        if(s[j] not in d.keys()):
            d[s[j]]=1
        else:
            d[s[j]]+=1
    if(len(d)>k):
        if(j-i>m):
            m=j-i
        while(len(d)>k):
            d[s[i]]-=1
            if(d[s[i]]==0):
                d.pop(s[i])
            i+=1
    j+=1
    if(len(d)==k and j==len(s)):
        if(j-i>m):
            m=j-i
print(m)
        
        
        
        
        
    
