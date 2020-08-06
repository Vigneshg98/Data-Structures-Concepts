class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


class LiList :
    def __init__(self) :
        self.head = None

    def push(self, data) :
        node = Node(data)
        node.next = self.head
        self.head = node

    def display(self) :
        temp = self.head
        while temp :
            print(temp.data, end = " ")
            temp = temp.next

    def reverse(self) :
        prev = None
        cur = self.head
        while cur is not None :
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev


if __name__ == "__main__" :
    li = LiList() 
    li.push(20) 
    li.push(4) 
    li.push(15) 
    li.push(85) 
      
    li.reverse() 
    li.display()
