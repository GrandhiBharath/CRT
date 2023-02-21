def changecase(s,op):
    if(len(s)==0):
        print(op)
        return
    else:
        op1=op+s[0]
        op2=op+s[0].upper()
        s=s[1:]
        changecase(s,op1)
        changecase(s,op2)
        return
s=input()
op=""
changecase(s,op)
    
