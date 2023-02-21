l=list(map(int,input().split()))
k=int(input())
t=[]
i,j=0,0
while(j<len(l)):
    if(len(t)==0):
        t.append(l[j])
    else:
        while(len(t)>0 and l[j]<t[-1]):
            t.pop(-1)
        t.append(l[j])
        if((j-i+1)==k):
            print(t[0],end=" ")
            if(l[i]==t[0]):
                t.pop(0)
            i+=1
    j+=1
            
            
        
   
