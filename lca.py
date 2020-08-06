class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def findPath(root,n,path):

    if (root is None):
        return False
    
    path.append(root.key)
    
    if(root.key == n):
        return True

    
    if(root.left!= None and findPath(root.left,n,path) or root.right!= None and findPath(root.right,n,path)):
        return True
    path.pop()
    return False
        

def findLca(root,n1,n2):
    path1=[]
    path2=[]
    i=0
    if(not findPath(root,n1,path1) or not findPath(root,n2,path2)):
        return -1
    while(i<len(path1) or len(path2)):
        if(path1[i]!=path2[i]):
            break
        i+=1
    return path1[i-1]
    

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
print(findLca(root,4,6))
