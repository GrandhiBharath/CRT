s1=input()
s2=input()
s1="0"+s1
s2="0"+s2
m=[]
for i in range(len(s2)):
    t=[0]*(len(s1))
    m.append(t)
for i in range(1,len(s2)):
    for j in range(1,len(s1)):
        if(s2[i]==s1[j]):
            m[i][j]=1+m[i-1][j-1]
for i in range(len(s2)):
    for j in range(len(s1)):
        print(m[i][j],end=" ")
    print()
ma=0
for i in range(len(s2)):
    for j in range(len(s1)):
        if(m[i][j]>ma):
            ma=m[i][j]
a=len(s1)-ma-1
b=len(s2)-ma-1
print(a+b+ma)
         
        
            

        
            
        
