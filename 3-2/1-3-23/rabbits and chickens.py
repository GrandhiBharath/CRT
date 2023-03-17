h,l=map(int,input().split())
if(h>l or l%2!=0):
    print("invalid")
else:
    print("no of chickens:",(4*h - l)//2)
    print("no of rabbits:",(l - 2*h)//2)
