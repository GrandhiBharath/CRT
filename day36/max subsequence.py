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
            a=m[i-1][j-1]+1
            m[i][j]=a
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
for i in range(len(s2)):
    for j in range(len(s1)):
        print(m[i][j],end=" ")
    print()
print("Maximum length subsequence: ",m[len(s2)-1][len(s1)-1])
b=m[len(s2)-1][len(s1)-1]
s=''
j=len(s1)-1
i=1
while(b!=0):
    if(i==len(s2)):
        i=1
        j=j-1
    if(m[i][j]!=m[i][j-1]):
        s=s1[j]+s
        i=1
        j=j-1
        b=b-1
    else:
        i=i+1
print(s)
        
            
        
