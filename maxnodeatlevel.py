from queue import Queue
class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None


def maxnodeatlevel(root):
    if root is None:
        return -1
    q=Queue()
    q.put(root)
    level=0
    m_level=0
    max=-99999999999
    while(1):
        nodecount=q.qsize()
        if nodecount == 0 :
            break
        if max<nodecount:
            max=nodecount
            m_level=level
        while(nodecount>0):
            node=q.queue[0]
            q.get()
            if(node.left!=None):
                q.put(node.left)
            if(node.right!=None):
                q.put(node.right)
            nodecount-=1
        level+=1
    return max,m_level

root=node(2)
root.left=node(1)
root.right=node(3)
root.right.right=node(8)
root.left.left=node(4)
root.left.right=node(6)
root.left.right.right=node(5)
print(maxnodeatlevel(root))
