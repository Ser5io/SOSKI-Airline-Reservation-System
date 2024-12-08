from node import Node

class Queue :
    def __init__(self):
        self.head = self.tail = None
        self.counter = 0
    
    # Checks if the queue is empty.    
    def isEmpty(self):
        return self.head == None
    
    # Adds a node to the end of the queue.
    def enqueue(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    # Removes a node from the front of the queue.    
    def dequeue(self):
        if self.isEmpty():
            return
        else:
            node = self.head
            self.head = self.head.next
            node.prev = node.next = None
            return node.data

    # Returns the front of the queue.
    def getFront(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
        
    def getSize (self):
        pass
    def display(slef):
        pass
    def clear(self):
        pass
    def reverse(self):
        pass
        
