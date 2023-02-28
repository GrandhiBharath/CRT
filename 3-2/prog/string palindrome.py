s1=input()
s2=input()
f=[0]*26
f1=[0]*26
s1.lower()
s2.lower()
if(len(s1)<len(s2)):
    s1,s2=s2,s1
for i in s1:
    f[ord(i)-97]+=1
for i in s2:
    f1[ord(i)-97]+=1
o,e=0,0
for i in s2:
    f1[ord(i)-97]-=1
    f[ord(i)-97]-=1
c=0
for i in f:
    if(i<0):
        c=1
        break
if(c==1):
    print("NO")
else:
    for i in f:
        if(i>0):
            if(i%2!=0):
                o+=1
            else:
                e+=1
    if(o==1 or o==0 or e>0):
        print("YES")
    else:
        print("NO")
    
        
        
    
