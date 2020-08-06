class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def isBST(root, l, r) :
    if root is None :
        return True
    print(root.data, l, r)
    print("")
    if l is not None and root.data < l.data :
        return False
    if r is not None and root.data > r.data :
        return False
    return isBST(root.left, l, root) and isBST(root.right, root, r)


if __name__ == '__main__' : 
    root = Node(3)  
    root.left = Node(2)  
    root.right = Node(5)  
    root.right.left = Node(1)  
    root.right.right = Node(4)  
    #root.right.left.left = Node(40) 

    if isBST(root, None, None) : 
        print("Is BST") 
    else : 
        print("Not a BST") 
