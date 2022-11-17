s=input()
l=[]
def rev(n):
    a=""
    for i in range(len(n)-1,-1,-1):
        a=a+n[i]
    return a
s1=""
for i in s:
    if(i!=" "):
        s1=s1+i
    else:
        print(rev(s1),end=" ")
        s1=""
print()
s2=""
for i in range(len(s)-1,-1,-1):
    if(s[i]!=" "):
        s2=s2+s[i]
    else:
        print(rev(s2),end=" ")
        s2=""
    if(i==0):
        print(rev(s2))
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")


