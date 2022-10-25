l=list(map(int,input().split()))
k=int(input())
if(len(l)%2!=0):
    print("false")
else:
    l1=[0]*k
    c=0
    for i in l:
        a=i%k
        l1[a]=l1[a]+1
    i=1
    j=k-1
    f=0
    while(i<j):
        if(l1[i]!=l1[j]):
            f=1
            break
        i=i+1
        j=j-1
    if(k%2==0):
        if(l1[0]%2!=0 or l1[k//2]%2!=0):
            f=1
    else:
        if(l1[0]%2!=0):
            f=1
    if(f==1):
        print("false")
    else:
        print("true")
    
    
    

    
    
    
