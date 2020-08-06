class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None


def height(root, ans) :
    if root is None :
        return 0
    lHeight = height(root.left, ans)
    print("left", lHeight)
    rHeight = height(root.right, ans)
    print("Right", rHeight)
    ans[0] = max(ans[0], 1+lHeight+rHeight)
    print(ans)
    return 1 + max(lHeight, rHeight)


def diameter(root) :
    if root is None :
        return 0
    ans = [-999]
    height(root, ans)
    return ans[0]


if __name__ == '__main__' : 
    root = Node(1)  
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5)
    root.right.right = Node(7)
    print(diameter(root))
