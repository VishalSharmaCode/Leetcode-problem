class Node:
    def __init__(self, data):
        self.data = data
        self.head = None 
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
