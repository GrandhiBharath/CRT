l=list(map(int,input().split()))
a=int(input("enter the sum"))
op=[]
m1=[]
m=0
def sumarray(l,op,a,m1,m):
    if(len(l)==0):
        if(sum(op)==a):
            print(sum(op),op,sep=" ")
        elif(sum(op)<a and sum(op)>m):
            m=sum(op)
            m1.append(op)
        return m
    else:
        op1=op.copy()
        op2=op.copy()
        op2.append(l[0])
        l=l[1:]
        m=sumarray(l,op1,a,m1,m)
        m=sumarray(l,op2,a,m1,m)
        return m
m=sumarray(l,op,a,m1,m)
print(m,m1[-1],sep=" ")


    
