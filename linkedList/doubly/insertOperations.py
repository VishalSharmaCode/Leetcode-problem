class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Insert At End
    def tailInsert(self, data):
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = new_node
            self.tail = new_node
            return 
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    
    # Insert at head
    def headInsert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    #Insert at position
    def posInsert(self, pos, data):
        new_node = Node(data)
        if pos == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            return
        current = self.head
        count = 0
        while current is not None and count < pos-1:
            current = current.next
            count+=1
        if current is None:
            print('Possition is out of bounds')
            return 
        
        if current.next is None:
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
            return
        
        next_node = current.next
        new_node.next = next_node
        new_node.prev = current
        
        next_node.prev = new_node
        current.next = new_node
        
        
    # Display  
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')
        
ll = LinkedList()
ll.headInsert(10)
ll.headInsert(20)
ll.headInsert(30)

ll.posInsert(2,56)
ll.display()

