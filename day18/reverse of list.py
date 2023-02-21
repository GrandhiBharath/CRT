'''
def reverse(l):
    if(len(l)==0):
        return
    else:
        t=l.pop(-1)
        print(t,end=" ")
        reverse(l)
        return
l=list(map(int,input().split()))
reverse(l)
'''

def rev(l):
    if(len(l)==0):
        return
    else:
        t=l.pop(0)
        rev(l)
        l.append(t)
        return l
l=list(map(int,input().split()))
a=rev(l)
print(l)
