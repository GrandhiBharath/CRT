s=input()
c=0
for i in s:
    if((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57)):
        continue
    else:
        c=c+1
print(c)
