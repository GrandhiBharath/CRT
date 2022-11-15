s=input()
d={}
c=0
for i in range(97,123):
    d[chr(i)]=0
s=s.lower()
for i in s:
    if(i in d.keys()):
        d[i]+=1
for i in d.values():
    if(i==0):
        c=1
        break
if(c==0):
    print("pangram")
else:
    print("not pangram")

    

