from queue import Queue
q = Queue()
q1 = Queue()
class node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def printleafnode(root) :
    if root is None :
        return

    if(root.left is None and root.right is None) :
        q1.put(root.data)
    else:
        q.put(root.data)
        root.left = printleafnode(root.left)
        root.right = printleafnode(root.right)
    
def disp() :
    print("Leaf Nodes")
    for i in range(q1.qsize()) :
        print(q1.queue[i])
    print("Internal Nodes")
    for i in range(q.qsize()) :
        print(q.queue[i])
    
  
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

printleafnode(root)
disp()
