def reverse(n,s):
    if(n==0):
        return s
    else:
        r=n%10
        s=s*10+r
        n=n//10
        return reverse(n,s)
n=int(input())
s=0
print(reverse(n,s))
