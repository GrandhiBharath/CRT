n=int(input())
l=[0]*(n)
l[0]=0
l[1]=1
def fibo(n,l):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        for i in range(2,n):
            l[i]=l[i-1]+l[i-2]
        return l[n-1]
print(fibo(n,l))
