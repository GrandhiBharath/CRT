p=1
for i in range(1,8):
    for j in range(1,6):
        if(j<=p):
            print(" ",end='')
        else:
            print("*",end='')
    print()
    if(i<4):
        p=p+1
    else:
        p=p-1
    
