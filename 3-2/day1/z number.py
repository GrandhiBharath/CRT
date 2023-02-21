s=input()
if(int(s[0])<int(s[1])):
    k=0
else:
    k=1
c=0
for i in range(k,len(s)-1):
    if(c==0 and int(s[i])<int(s[i+1])):
        c=1
    elif(c==1 and int(s[i])>int(s[i+1])):
        c=0
    else:
        c=3
        break
if(c==3):
    print('NO')
else:
    print('YES')
        
