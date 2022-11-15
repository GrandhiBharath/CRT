s=input()
d={}
for i in s:
    if((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57)):
        continue
    else:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
for i in d.keys():
    print(i,'->',d[i])
