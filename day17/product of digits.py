def product(n,p):
    if(n==0):
        return p
    else:
        r=n%10
        p=p*r
        n=n//10
        a=product(n,p)
        return a
n=int(input())
p=1
print(product(n,p))
