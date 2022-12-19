l=list(map(int,input().split()))
a=int(input("enter the sum"))
op=[]
def sumarray(l,op,a):
    if(len(l)==0 or sum(op)>=a):
        if(sum(op)==a):
            print(op)
        return
    else:
        op1=op.copy()
        op2=op.copy()
        op2.append(l[0])
        l=l[1:]
        sumarray(l,op1,a)
        sumarray(l,op2,a)
        return
sumarray(l,op,a)

    
