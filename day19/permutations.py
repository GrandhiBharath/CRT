def permutations(ip,op):
    if(len(ip)==0):
        print(op)
        return
    else:
        for i in range(len(ip)):
            nop=ip[i]
            nip=ip[0:i]+ip[i+1:]
            permutations(nip,op+nop)
        return
ip=input()
permutations(ip,'')
