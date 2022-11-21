n=int(input())
l1=[0]*5
l2=[0]*5
i,j=0,0
a=n//10
b=n%10
while(a>0):
    if(a<=4):
        l1[a-1]+=1
    if(a==5):
        l1[4]=1
        break
    else:
        l1[4]=1
        a=a%5
        a+=1
    a-=1
if(b>0):
    if(b<=4):
        while(b<=4):
            l2[b]+=1
            b+=1
    if(b==5):
        l1[0]+=1
    else:
        l1[0]=1
        b=b
    
    

  
