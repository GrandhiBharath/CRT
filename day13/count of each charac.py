s=input()
d={}
for i in s:
    if i not in d.keys():
            d[i]=1
    else:
            d[i]+=1
for i in d.keys():
    print(i,'->',d[i])
