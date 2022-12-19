n=int(input())
def fibo(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        m=fibo(n-1)+fibo(n-2)
        return m
m=fibo(n)
print(m)
    
