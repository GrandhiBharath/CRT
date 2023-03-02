n=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(len(l)):
    if(l[-1]<sum(l[0:len(l)-1])):
       print(sum(l))
       break
    else:
        l.pop()

'''they will give sides from those we need to choose a polygon having largest perimeter
   condition is one side is less than sum of other'''
