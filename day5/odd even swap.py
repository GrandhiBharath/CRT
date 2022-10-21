'''l=list(map(int,input().split()))
i=0
j=len(l)-1
while(i<j):
   if(l[i]%2==0 and l[j]%2!=0):
       i=i+1
       j=j-1
   if(l[i]%2==0 and l[j]%2==0):
       i=i+1
   if(l[i]%2!=0 and l[j]%2==0):
       t=l[i]
       l[i]=l[j]
       l[j]=t
       i=i+1
       j=j-1
   if(l[i]%2!=0 and l[j]%2!=0):
       j=j-1
print(l)'''


l=list(map(int,input().split()))
i=0
j=len(l)-1
while(i<j):
    if(l[i]%2!=0 and l[j]%2==0):
        t=l[i]
        l[i]=l[j]
        l[j]=t
        i=i+1
        j=j-1
    if(l[i]%2==0):
        i=i+1
    if(l[j]%2!=0):
        j=j-1
print(l)
   
    
