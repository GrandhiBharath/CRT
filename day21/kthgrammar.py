def kthgrammar(n,k):
    if(n==1 and k==1):
        return 0
    else:
        m=(2**(n-2))
        l=m*2
        if(k>l):
            return "invalid"
        if(k<=m):
            t=kthgrammar(n-1,k)
            return t
        else:
            t=kthgrammar(n-1,k-m)
            if(t==0):
                return 1
            else:
                return 0
n,k=map(int,input().split())
print(kthgrammar(n,k))
