def subset(ip,op):
    if(len(ip)==0):
        print(op)
        return
    else:
        op1=op
        op2=op+ip[0]
        ip=ip[1:]
        subset(ip,op1)
        subset(ip,op2)
        return
s=input()
subset(s,"")
