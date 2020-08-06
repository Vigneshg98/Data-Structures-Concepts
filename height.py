class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def maxDepth(root):
    if(root is None):
        return 0
    else:
        ldepth=maxDepth(root.left)
        #print("l ", ldepth)
        rdepth=maxDepth(root.right)
        #print("r ", rdepth)
        if(ldepth>rdepth):
            return ldepth+1
        else:
            return rdepth+1
  
root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(60)
root.right.right=Node(80)
print(maxDepth(root))
