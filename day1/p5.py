n=int(input())
a=97
b=65
c=122
d=90
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i%2!=0):
            print(chr(a),chr(b),sep="",end=" ")
            a=a+1
            b=b+1
        else:
            print(chr(c),chr(d),sep="",end=" ")
            c=c-1
            d=d-1
    if(i%2!=0):
        a=a-(n-1)
        b=b-(n-1)
    else:
        c=c+(n-1)
        d=d+(n-1)
    print()
            
