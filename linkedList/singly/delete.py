class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Head Delete
    def delete_head(self):
        current = self.head
        if current is None:
            print('Already Empty')
            return
        self.head = self.head.next
        print('Removed Successfully')
    
    # Tail Delete
    def tail_delete(self):
        current = self.head
        if current is None:
            print('List is Already Empty')
            return
        if current.next is None:
            self.head = None
            return
        while current.next.next is not None:
            current = current.next
        current.next = None
    
    # def by_position(self, pos):
        
        
    def display(self):
        current = self.head
        if current is None:
            print('Empty List')
            return
        print('Linked List Elements:', end = ' ')
        
        while current is not None:
            print(current.data, end = ' -> ')
            current = current.next
        print('None')
        
ll = LinkedList()
for i in range(10, 0, -1):
    ll.insert(i)
print('-----Before Delete-----')
ll.display()

ll.delete_head()
print('-----After Delete-----')
ll.tail_delete()
ll.display()
