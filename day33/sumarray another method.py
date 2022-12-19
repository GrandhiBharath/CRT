l=list(map(int,input().split()))
a=int(input("enter the sum"))
s=0
def sumarray(l,a,s):
    if(len(l)==0 or a==0):
        return s
    else:
        if(a>=l[0]):
            op1=sumarray(l[1:],a,s)
            op2=sumarray(l[1:],a-l[0],s+l[0])
            return max(op1,op2)
        else:
            op=sumarray(l[1:],a,s)
            return op
m=sumarray(l,a,s)
print(m)
    
