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
s=""
for i in range(len(s2)):
    for j in range(len(s1)):
        a=i
        b=j
        while(m[a][b]>0):
            s=s2[a]+s
            a=a-1
            b=b-1
        if(len(s)!=0):
            print(s,end=" ")
        s=""
        
            

        
            
        
