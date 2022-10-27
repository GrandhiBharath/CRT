l=list(map(int,input().split()))
k=int(input())
i,j=0,0
while(j<len(l)):
    if(l[j]<0):
        print(l[j],end=" ")
        if(j==(len(l)-1)):
            break
        i+=1
        j=i
    elif((j-i+1)==k):
        print("0",end=" ")
        if(j==(len(l)-1)):
            break
        i=i+1
        j=i
    else:
        j=j+1
        
    
