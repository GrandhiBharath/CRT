p=q=4
for i in range(1,8):
    for j in range(1,8):
        if(j<=p):
            print("*",end='')
        elif(j>p and j<q):
            print(' ',end='')
        else:
            print("*",end='')
    if(i<4):
        p=p-1
        q=q+1
    else:
        p=p+1
        q=q-1
    print()
