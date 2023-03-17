s=input()
p=len(s)
for i in range(1,p+1):
    for j in range(i):
        print(s[j],end=" ")
    print()
