def palindrome(n,s,m):
    if(m==-1):
        return s
    else:
        s=s+n[m]
        m-=1
        a=palindrome(n,s,m)
        return a
n=input()
s=""
m=len(n)-1
v=palindrome(n,s,m)
if(v==n):
    print("palindrome")
else:
    print("not palindrome")
