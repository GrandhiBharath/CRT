def underscore(s,op):
    if(len(s)==0):
        print(op)
    else:
        op1=op+s[0]
        op2=op+"_"+s[0]
        s=s[1:]
        underscore(s,op1)
        underscore(s,op2)
s=input()
op=s[0]
underscore(s[1:],op)
