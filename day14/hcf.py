x,y=map(int,input().split())
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
print(v)
