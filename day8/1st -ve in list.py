l=list(map(int,input().split()))
k=int(input())
i,j=0,0
t=[]
while(j<len(l)):
    if((j-i+1)<k):
        j+=1
    if(l[j]<0): 
        t.append(l[j])
    if((j-i+1)==k):
        if(len(t)==0):
            print("0",end=" ")
        else:
            if(t[0]==l[i]):
                print(t.pop(0),end=" ")
            else:
                print(t[0],end=" ")
        i+=1
        j+=1
        
    
        
        

    
