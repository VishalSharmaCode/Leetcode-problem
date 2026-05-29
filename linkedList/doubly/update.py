class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Update by Index
    def indexUpdate(self, pos, new_data):
        current = self.head
        count = 0
        while current is not None:
            if count == pos:
                current.data = new_data
                return 
            current = current.next
            count += 1
        print('Out Of bound')
        return
    def valueUpdate(self, old_value, new_value):
        current = self.head
        while current is not None:
            if current.data == old_value:
                current.data = new_value
                return True
            current = current.next
        print("Value not found")
        return 
                
        
    # Insert At End
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node   
    
        
    # Display
    def display(self):
        if self.head is None:
            print('List is empty')
            return 
        current = self.head
        print('list element: ', end = " ")
        
        while current is not None:
            print(current.data, end = ' -> ')
            current = current.next
        print('None')
        
ll = LinkedList()
for i in range(5):
    ll.insert_at_end(i)

print('Original List')
ll.display()

ll.indexUpdate(2,44)
print('Changed List index update')
ll.display()

ll.valueUpdate(3,88)
ll.display()
