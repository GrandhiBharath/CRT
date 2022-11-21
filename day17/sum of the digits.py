def sum(n,s):
    if(n==0):
        return s
    else:
        r=n%10
        s=s+r
        n=n//10
        a=sum(n,s)
        return a
n=int(input())
s=0
print(sum(n,s))

