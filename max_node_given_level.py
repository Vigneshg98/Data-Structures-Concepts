class node :
    def __init__(self,key) :
        self.key = key
        self.left = None
        self.right = None

def maxnodevalue(root, level) :
    if root is None :
        return 0
    if level == 0 :
        return root.key
    lmax = maxnodevalue(root.left, level-1)
    #print("L ", lmax)
    rmax = maxnodevalue(root.right, level-1)
    #print("R ", rmax)
    return max(lmax, rmax)

root = node(2)
root.left = node(1)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(6)
root.right.right = node(8)
root.left.right.right = node(5)
root.left.right.left = node(7)
print(maxnodevalue(root, 3))
