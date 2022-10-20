p=q=3
for i in range(1,6):
    for j in range(1,6):
        if(j>=p and j<=q):
            print("*",end='')
        else:
            print(" ",end='')
    if(i<3):
        p=p-1
        q=q+1
    else:
        p=p+1
        q=q-1
    print()
