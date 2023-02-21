def table(n,i):
    if(i!=0):
        i-=1
        table(n,i)
        print(n*(i+1))
    else:
        return      
n=int(input())
i=int(input())
table(n,i)
    
