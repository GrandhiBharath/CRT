def changecase1(l,s,op):
    if(len(s)==0):
        l.append(op)
        return 
    else:
        if(ord(s[0])>=65 and ord(s[0])<=90):
            op1=op+s[0]
            op2=op+s[0].lower()
        if(ord(s[0])>=97 and ord(s[0])<=122):
            op1=op+s[0]
            op2=op+s[0].upper()
        if(ord(s[0])>=48 and ord(s[0])<=57):
           op1=op+s[0]
           op2=op+s[0]
        s=s[1:]
        changecase1(l,s,op1)
        changecase1(l,s,op2)
        return 
s=input()
op=""
l=[]
changecase1(l,s,op)
l=set(l)
for i in l:
    print(i)
