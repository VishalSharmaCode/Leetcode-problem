class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    
    def deleteFront(self):
        if self.head is None:
            print('List is allready empty')
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        else:
            self.head = self.head.next
            self.head.prev = None
            
    def delete_end(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.prev = None
    
    def delete_Pos(self, pos):
        if self.head is None:
            print('List is empty')
            return
        if pos == 0:
            self.deleteFront()
            return
        current = self.head
        count = 0
        while current is not None and count < pos:
            current = current.next
            count +=1
        if current is None:
            print('Position not found')
            return
        if current == self.tail:
            self.delete_end()
            return
        current.prev.next = current.next
        current.next.prev = current.prev
        current = None
    
    def delete_val(self, val):
        current = self.head
        while current is not None and current.data != val:
            current = current.next
        if current == self.head:
            self.deleteFront()
            return
        if current == tail:
            self.delete_end()
            return 
        current.prev.next = current.next
        current.next,prev = current.prev
        current = None
        
        
        
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')
    

ll = LinkedList()
for i in range(2,20,2):
    ll.append(i)

print('This is the original list')
ll.display()

print('Head removed')
ll.deleteFront()
ll.display()

ll.delete_Pos(1)
ll.display()