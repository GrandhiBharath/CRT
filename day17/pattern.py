def pattern(i,n):
   if(i>n):
       return 
   else:
       print(i)
       pattern(i+1,n)
       print(i)
i=int(input())
n=int(input())
pattern(i,n)
   
