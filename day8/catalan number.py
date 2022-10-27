n=int(input())
l=[1]*2
for k in range(0,n-2):
    s=0
    i=0
    j=len(l)-1
    while(i<=j):
        if(i==j):
            s=s+(l[i]*l[j])
            break
        s=s + (2*(l[i]*l[j]))
        i+=1
        j-=1
    l.append(s)
print(l)

        
    
