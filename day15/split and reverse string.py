s=input()
l=s.split(" ")
for i in l:
    print(i[::-1],end=" ")
print()
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")
print()
for i in range(len(l)-1,-1,-1):
    print(l[i][::-1],end=" ")
    
