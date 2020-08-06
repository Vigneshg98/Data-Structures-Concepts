from queue import Queue
class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None


def oddandeven(root):
    if(root is None):
        return root
    q=Queue()
    qodd=Queue()
    qeven=Queue()
    q.put(root)
    level=0
    i=0
    flag=0
    li=[]
    while(1):
        nodecount=q.qsize()
        if (nodecount == 0):
            break
        level+=1
        #print(level)
        if(level%2 != 0):
            qeven.put(level)
            flag=1
        else:
            qodd.put(level)
            flag=0
        
        while(nodecount>0):
            temp=q.queue[0]
            #print(temp.key)
            #print(q.get().key)
            li.append(q.get())
            if(temp.left is not None):
                q.put(temp.left)
            if(temp.right is not None):
                q.put(temp.right)
            nodecount-=1
        if(flag==0):
            li=li[::-1]
            for i in li:
                print(i.key,end=" ",sep=" ")
        elif(flag==1):
            for i in li:
                print(i.key,end=" ",sep=" ")
        #print(flag)
        li=[]
    """print("Even")
    for i in range(qeven.qsize()):
        print(qeven.get())
    print("Odd")
    for i in range(qodd.qsize()):
        print(qodd.get())"""
    


root=node(7)
root.left=node(6)
root.right=node(5)
root.left.left=node(4)
root.right.left=node(3)
root.right.left.right=node(1)
root.left.left.left=node(2)
oddandeven(root)
