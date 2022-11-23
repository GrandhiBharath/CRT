def fun(l,op,k):
    if(sumoflist(op,0,0)==k):
        print(op)
        return
    else:
        op1=op.copy()
        op2=op.copy()
        op2.append(l[0])
        l=l[1:]
        fun(l,op1,k)
        fun(l,op2,k)
        return
def sumoflist(op,i,s):
    if(i==len(op) or len(op)==0):
        return s
    else:
        s=s+l[i]
        i+=1
        sumoflist(l,i,s)
l=list(map(int,input().split()))
k=int(input())
op=[]
fun(l,op,k)
