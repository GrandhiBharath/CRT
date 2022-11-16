l=list(map(int,input().split()))
x=l[0]
y=l[1]
def hcf(a,b):
    r=a%b
    while(r!=0):
        a=b
        b=r
        r=a%b
    return b
if(x>y):
    v=hcf(x,y)
else:
    v=hcf(y,x)
for i in range(2,len(l)):
    if(v>l[i]):
        v=hcf(v,l[i])
    else:
        v=hcf(l[i],v)
print(v)
    
