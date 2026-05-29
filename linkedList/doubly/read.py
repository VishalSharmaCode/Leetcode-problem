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
    
    # Read All
    def read_all(self): # Forward
        current = self.head
        while current is not None:
            print(current.data , end=' <-> ')
            current = current.next
        print('None')
        
    def read_all_back(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print('None')
        
    # Read By position
    def readPosition(self, pos):
        current = self.head
        count = 0
        while current is not None:
            if count == pos:
                print(current.data)
                return
            count +=1
            current = current.next
        print('Position is not in List')
        return 
    
    # Read by value
    def readValue(self, value):
        current =self.head
        count = 0
        while current is not None:
            if current.data == value:
                print(count)
                return
            count +=1
            current = current.next
        print('Value Not found')
        return
ll = LinkedList()

for i in range(10):
    ll.append(i)
print('Read from Front')
ll.read_all()
print('Read from back') 
ll.read_all_back()  
print('Print by position')
ll.readPosition(4)   
print('Print by value')
ll.readValue(3)
  