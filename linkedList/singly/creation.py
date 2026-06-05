class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    # Insert At Front
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
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
        
    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current is not None and count< pos-1:
            current = current.next
            count +=1
        if current is None:
            print('Possition is out of bound')
            return
        new_node.next = current.next
        current.next = new_node
    
    
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
ll.insert_at_pos(10,0)
ll.insert_at_pos(20,1)
ll.insert_at_pos(30,1)

ll.display()
