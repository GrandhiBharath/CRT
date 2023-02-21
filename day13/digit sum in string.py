s=input()
i,t,f=0,0,0
while(i<len(s)):
    if(ord(s[i])>=48 and ord(s[i])<=57):
        t=t*10 + int(s[i])
    else:
        f=f+t
        t=0
    i+=1
f=f+t
print(f)
            
    
