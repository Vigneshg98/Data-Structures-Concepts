class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def minvalueNode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
        
def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print(root.key) 
        inorder(root.right)
        
def deletion(root,key):
    #Base Condition
    if(root is None):
        return root
    if(key<root.key):
        root.left=deletion(root.left,key)
    elif(key>root.key):
        root.right=deletion(root.right,key)
    else:
        #if it has one or no child
        if(root.left is None):
            temp=root.right
            root=None
            return temp
        elif(root.right is None):
            temp=root.left
            root=None
            return temp
        #if it has two child
        #Need to find inorder succesor
        temp=minvalueNode(root.right)
        root.key=temp.key
        root.right=deletion(root.right,temp.key)
    return root

root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(60)
root.right.right=Node(60)
inorder(root)
print("")
t=deletion(root,20)
inorder(t)
