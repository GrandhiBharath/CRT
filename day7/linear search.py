l=list(map(int,input().split()))
n=int(input())
a=0
for i in range(0,len(l)):
    if(l[i]==n):
        a=1
        b=i+1
        break
if(a==1):
    print(b)
else:
    print("-1")
    
