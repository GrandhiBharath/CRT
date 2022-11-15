s1=input()
s2=input()
d={}
c=0
if(len(s1)==len(s2)):
    for i in s1:
        if(i not in d.keys()):
            d[i]=1
        else:
            d[i]+=1
    for i in s2:
        if(i in d.keys()):
            d[i]-=1
        else:
            c=1
            break
    for i in d.values():
        if(i!=0):
            c=1
            break
    if(c==1):
        print("not anagram")
    else:
        print("anagram")
else:
    print("not anagram")
    
        

            
    
