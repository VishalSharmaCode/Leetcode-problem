class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    # Read all Elements of Linked List
    def read_all(self):
        if self.head is None:
            print('List is Empty')
            return 
        current = self.head
        print('Linked List Elements:', end = ' ')
        
        while current is not None:
            print(current.data, end = ' -> ')
            current = current.next
        print('None')
    
    # Access by Index
    def by_index(self, pos):
        current = self.head
        count = 0
        while current:
            if count == pos:
                print('Value ->',current.data)
                return 
            count += 1
            current = current.next
        print("Index Out Of range")
        return 
    
    # Access By value
    def by_value(self, value):
        current = self.head
        count = 0
        while current:
            if current.data == value:
                print('Position of value :-', count)
                return
            count += 1
            current = current.next
        print('Value Not Found')
        return

ll = LinkedList()

for i in range(0, 11, 2):
    ll.insert_at_end(i)
print('----Print All Elements Of LL----')
ll.read_all()
print(' ')
print('----Print value by index----')
ll.by_index(4)
print(' ')
print('----Print index By Value----')
ll.by_value(0)



