class bst:
    def __init__(self,value):
        self.left=None
        self.value=value
        self.right=None
root=None
def insert(value,root):
    l=bst(value)
    if(root==None):
        root=l
    else:
        p=root
        while(1):
            if(value==p.value):
                print("\nrepeated elements cant be inserted\n")
                return root
            elif(value<p.value and p.left!=None):
                p=p.left
            elif(value>p.value and p.right!=None):
                p=p.right
            else:
                break
        if(value<p.value):
            p.left=l
        else:
            p.right=l
    return root
def inorder(p):
    if(p==None):
        print("empty")
        return
    else:
        if(p.left!=None):
            inorder(p.left)
        print(p.value)
        if(p.right!=None):
            inorder(p.right)
def preorder(p):
    if(p==None):
        print("empty")
        return
    else:
        print(p.value)
        if(p.left!=None):
            preorder(p.left)
        if(p.right!=None):
            preorder(p.right)
def postorder(p):
    if(p==None):
        print("empty")
        return
    else:
        if(p.left!=None):
            postorder(p.left)
        if(p.right!=None):
            postorder(p.right)
        print(p.value)
def delete(p,value,q):
    if(p==None):
        print("empty")
        return
    else:
        if(value<p.value):
            q=p
            if(p.left!=None):
                delete(p.left,value,q)
        elif(value>p.value):
            q=p
            if(p.right!=None):
                delete(p.right,value,q)
        elif(value==p.value):
            if(p.left==None and p.right==None):
                if(q.right!=None):
                    q.right=None
                else:
                    q.left==None
                del(p)
            elif(p.left!=None and p.right==None):
                if(p.value>q.value):
                    q.right=p.left
                    del(p)
                else:
                    q.left=p.left
                    del(p)
            elif(p.left==None and p.right!=None):
                if(p.value>q.value):
                    q.right=p.right
                    del(p)
                else:
                    q.left=p.right
                    del(p)
            elif(p.left!=None and p.right!=None):
                print("1.inorder successor","2.inorder preccessor",sep="\n")
                b=int(input("choose your choice"))
                if(b==1):
                    s=p.right
                    while(s.left!=None):
                        s=s.left
                    p.value=s.value
                    
                    
                    
                        
                
while(1):
    print("1.insert","2.inorder","3.preorder","4.postorder","5.delete",sep="\n")
    a=int(input("enter your choice"))
    if(a==1):
        l=list(map(int,input("enter the values").split()))
        for i in l:
            root=insert(i,root)
    elif(a==2):
        inorder(root)
    elif(a==3):
        preorder(root)
    elif(a==4):
        postorder(root)
    elif(a==5):
        value=int(input("enter the element to be deleted"))
        delete(root,value,root)
       
       
        
        
        
        
                
                
            
            
        
    
