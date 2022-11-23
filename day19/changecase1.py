def changecase1(l,s,op):
    if(len(s)==0):
        l.append(op)
        return 
    else:
        if(s[0].lower()!=s[0]):
            op1=op+s[0]
            op2=op+s[0].lower()
        else:
            op1=op+s[0]
            op2=op+s[0].upper()
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


        
            
