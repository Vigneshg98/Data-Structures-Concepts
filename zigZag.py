from queue import Queue

class Node :
    def __init__(self, data) :
        self.data = data
        self.left = self.right = None

def zigZag(root) :
    if root is None :
        return root

    q = Queue()
    q.put(root)
    li = []
    level = flag = 0
    
    while(1) :
        cnt = q.qsize()
        if cnt == 0 :
            break
        level+=1

        if level%2 == 0 :
            flag = 0
        else :
            flag = 1

        while cnt > 0 :
            tmp = q.queue[0]
            li.append(q.get())

            if tmp.left is not None :
                q.put(tmp.left)
            if tmp.right is not None :
                q.put(tmp.right)

            cnt-=1

        if flag == 0 :
            li = li[::-1]
            for i in li :
                print(i.data, end = " ")
        elif flag == 1 :
            for i in li :
                print(i.data, end = " ")
        li = []

    

if __name__ == "__main__" :
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    zigZag(root)
