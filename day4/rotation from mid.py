l=list(map(int,input().split()))
n=int(input("left rotation "))
m=int(input("right rotation"))
a=len(l)//2
n=n%a
m=m%(len(l)-a)
while(n!=0):
    t=l[a-1]
    for i in range(a-2,-1,-1):
        l[i+1]=l[i]
    l[0]=t
    n=n-1
while(m!=0):
    t=l[a]
    for i in range(a+1,len(l)):
        l[i-1]=l[i]
    l[len(l)-1]=t
    m=m-1
print(l)
    
