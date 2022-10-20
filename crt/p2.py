p=4
q=6
for i in range(1,5):
    for j in range(i,i+9):
        if(j<=p):
            print("*",end='')
        elif(j>p and j<q):
            print("@",end='')
        else:
            print("$",end='')
    q=q+2
    print()
