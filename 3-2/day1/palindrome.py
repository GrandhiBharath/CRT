n=int(input())
def palindrome(n):
    t=n
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    if(t==s):
        return 1
    else:
        return 0
def reverse(n):
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    return s
while(palindrome(n)!=1):
    n=n+reverse(n)
print(n)
        
        
