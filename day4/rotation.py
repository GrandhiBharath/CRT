l=list(map(int,input().split()))
n=int(input("left rotation"))
n=n%len(l)
while(n!=0):
    a=l[len(l)-1]
    for i in range(len(l)-2,-1,-1):
        l[i+1]=l[i]
    l[0]=a
    n=n-1
print(l)

'''
l=list(map(int,input().split()))
m=int(input("right rotation"))
while(m!=0):
    b=l1[0]
    for i in range(1,len(l1)):
        l1[i-1]=l1[i]
    l1[len(l1)-1]=b
    m=m-1
print(l1)'''
