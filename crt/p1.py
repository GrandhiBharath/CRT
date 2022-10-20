p=5
for i in range(1,5):
    for j in range(i,i+5):
        if(j<p):
            print("+",end='')
        else:
            print("*",end='')
    print()

