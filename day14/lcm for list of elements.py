l=list(map(int,input().split()))
x=l[0]
y=l[1]
p=x*y
def hcf(a,b):
    r=a%b
    while(r!=0):
        a=b
        b=r
        r=a%b
    return b
if(x>y):
    v=hcf(x,y)
    lcm=p//v
else:
    v=hcf(y,x)
    lcm=p//v
for i in range(2,len(l)):
    if(v>l[i]):
        v=hcf(v,l[i])
        lcm=lcm*l[i]//v
    else:
        v=hcf(l[i],v)
        lcm=lcm*l[i]//v
print(lcm)

