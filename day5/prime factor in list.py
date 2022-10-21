import math
l=list(map(int,input().split()))
l1=[]
for i in l:
    for j in range(2,i+1):
        if(i%j==0):
            if(j not in l1):
                l1.append(j)
            break
print(len(l1))
print(l1)




    
    

        
            
            
    
    
