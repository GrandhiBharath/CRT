l=list(map(int,input().split()))
i=c=0
j=len(l)-1
while(i<j):
    if(l[i]==l[j]):
        i=i+1
        j=j-1
    else:
        c=c+1
        break
    
if(c>0):
    print("no")
else:
    print("yes")

