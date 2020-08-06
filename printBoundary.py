class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def printLeaves(root) :
    if root :
        printLeaves(root.left)
        if root.left is None and root.right is None :
            print(root.data)
        printLeaves(root.right)

def printBLeft(root) : 
    if root :
        if root.left :
            print(root.data)
            printBLeft(root.left)
        elif root.right :
            print(root.data)
            printBLeft(root.right)

def printBRight(root) : 
    if root :
        if root.right :
            printBRight(root.right)
            print(root.data) 
        elif root.left :
            printBRight(root.left)
            print(root.data)

def printBoundary(root) :
    if root :
        print(root.data)
        printBLeft(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printBRight(root.right)


root = Node(20) 
root.left = Node(8) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
root.right = Node(22) 
root.right.right = Node(25) 
printBoundary(root)
