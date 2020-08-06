class Node :
    def __init__(self, ele) :
        self.ele = ele
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

    def hasLoop(self) :
        if self.head is None :
            return False

        slow = self.head
        fast = self.head.next

        while fast is not None :
            if fast.next is None :
                return False
            fast = fast.next.next
            slow = slow.next

            if slow == fast :
                return True
        return False
        

li = LiList()
li.push(20)
li.push(4)
li.push(15)
li.push(10)

li.head.next.next.next.next = li.head

if li.hasLoop() :
    print("Yes")
else :
    print("No")
