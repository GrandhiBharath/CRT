def sumofsubset(l,s,m):
    if(s==m):
        print(l)
        return
    if(len(l)==0):
        if(s==m):
            print(l)
            return
    else:
        op1=s
        op2=s+l[0]
        l.pop(0)
        sumofsubset(l,op1,m)
        sumofsubset(l,op2,m)
        return
l=list(map(int,input().split()))
m=int(input())
s=0
sumofsubset(l,s,m)
