l=list(map(int,input("enter the weights").split()))
l1=list(map(int,input("enter the profits").split()))
k=int(input("enter the knapsack value"))
w=[]
p=0
m=0
m1=[]
def knapsack(l,l1,p,w,m,m1):
    if(len(l)==0):
        if(m<p):
            m=p
            m1.append(w)
        return m
    else:
        if(sum(w)<=k):
            p1=p
            p2=p+l1[0]
            w1=w.copy()
            w2=w.copy()
            w2.append(l[0])
            l=l[1:]
            l1=l1[1:]
            m=knapsack(l,l1,p1,w1,m,m1)
            m=knapsack(l,l1,p2,w2,m,m1)
        return m
m=knapsack(l,l1,p,w,m,m1)
print("The maximum profit and weights are:",m,m1[-1],sep=" ")
            
            
