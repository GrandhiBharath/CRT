a=int(input())
b=int(input())
def rev(n):
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    return s
v1=a+b
a1=rev(a)
b1=rev(b)
v2=a1+b1
v2=rev(v2)
if(v1==v2):
    print("energetic number")
else:
    print("not an energetic number")

        
