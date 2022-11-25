def quicksort(l,f,la):
    if(f<la):
        p=f
        i=f
        j=la
        while(i<j):
            while(l[i]<l[j]):
                i+=1
            while(l[j]>l[p]):
                j-=1
            if(i<j):
                l[i],l[j]=l[j],l[i]
        l[p],l[j]=l[j],l[p]
        quicksort(l,f,j-1)
        quicksort(l,j+1,la)
l=list(map(int,input().split()))
quicksort(l,0,len(l)-1)
print(l)
