a,b=map(int,input().split())
"with para with return"
def add(x,y):
    return x+y
v=add(a,b)
print(v)

"with para without return"
def add(x,y):
    print(x+y)
add(a,b)

"without para with return"
def add():
    p,q=map(int,input().split())
    return p+q
v=add()
print(v)

"without para without return"
def add():
    r,s=map(int,input().split())
    print(r+s)
add()


