def sort(l,i,j):
    if(len(l)==0 or len(l)==1):
        return l
    else:
        if(i==len(l)-1):
            return l
        if(j==len(l)-1):
            i+=1
            j=0
        elif(l[j]>l[j+1]):
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
            j+=1
        else:
            j+=1
        sort(l,i,j)
        return l
i,j=0,0
l=list(map(int,input().split()))
a=sort(l,i,j)
print(a)          
