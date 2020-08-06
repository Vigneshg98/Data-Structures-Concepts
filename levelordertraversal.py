from queue import Queue
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def levelorder(root):
    if root is None:
        return
    q=Queue()
    q.put(root)
    while(1):
        nodecount=q.qsize()
        if(nodecount == 0):
            break
        
        while(nodecount>0):
            node=q.queue[0]
            print(node.data)
            q.get()
            if(node.left is not None):
                q.put(node.left)
            if(node.right is not None):
                q.put(node.right)
            nodecount-=1


    
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
levelorder(root)
