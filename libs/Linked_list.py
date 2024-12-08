from node import Node

class Linked_list:
    def __init__(self):
        self.head = self.tail = None
        self.counter = 0
    
    # Prints a message if the list is empty.
    def emptyMsg(self):
        print('Empty list...!')
    
    # Checks if a specific position exists.
    def inRange(self, pos):
        return pos >=0 and pos < self.counter
    
    # Checks whether the function is empty or not.
    def isEmpty(self):
        return self.head == None
    
    # Adds a new node at the beginning of the list.
    def add(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            
        self.counter += 1
    
    # Adds a new node at the end of list.
    def append(self, data):
        newNode = Node(data)
        
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        
        self.counter += 1
    
    # Inserts a node at a specific position (if it exists).
    def insert(self, data, pos):
        if self.inRange(pos) or pos == self.counter:
            newNode = Node(data)
            if pos == 0:
                self.add(data)
            elif pos == self.counter:
                self.append(data)
            else:
                temp = self.head
                for i in range(pos):
                    temp = temp.next
                newNode.next = temp
                newNode.prev = temp.prev
                temp.prev.next = newNode
                
                self.counter += 1
        else:
            print('Out of Range...!')
    
    # Searchs if a specific node exists. If it does, it returns the position value.
    def search(self, data):
        if self.isEmpty():
            self.emptyMsg()
        else:
            temp = self.head
            pos = 0
            while temp:
                if temp.data == data:
                    return pos
                temp = temp.next
                pos += 1
            return -1
    
    # Prints out the list.
    def traverse(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            print('[',end=' ')
            temp = self.head
            while temp:
                print(temp.data,end=' ')
                temp = temp.next
            print(']')
    
    # Prints out the list in reversed order.
    def reverse(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            print('[',end=' ')
            temp = self.tail
            while temp:
                print(temp.data,end=' ')
                temp = temp.prev
            print(']')
    
    # Removes the head node and decrements the counter.
    def removeHead(self):
        if self.isEmpty():
            self.emptyMsg()
            return
        
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        del temp
        
        self.counter -= 1
    
    # Removes the tail node and decrements the counter.
    def removeTail(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del temp
            
            self.counter -= 1
    
    # Removes an item if it exists.
    def removeItem(self, data):
        if self.isEmpty():
            self.emptyMsg()
        else:
            pos = self.search(data)
            if pos == -1:
                print('item not found...!')
                return
            elif pos == 0:
                self.removeHead()
            elif pos == self.counter - 1:
                self.removeTail()
            else:
                temp = self.head
                for i in range(pos):
                    temp = temp.next
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                del temp
                
                self.counter -= 1
    
    # Clears the list.
    def clear(self):
        if self.isEmpty():
            self.emptyMsg()
        else:
            while self.head:
                temp = self.head
                self.head = self.head.next
                del temp 
            self.tail = self.head
            self.counter = 0
    
    # Removes a node at a specific position.        
    def removeAtPos(self, pos):
        if self.isEmpty():
            self.emptyMsg()
            return
        if self.inRange(pos):
            if pos == 0:
                self.removeHead()
            elif pos == self.counter - 1:
                self.removeTail()
            else:
                temp = self.head
                for i in range(pos):
                    temp = temp.next
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                del temp
                
                self.counter -= 1
        else:
            print('Out of range....!')
    
    # Removes the node(s) with a specific value
    def removeAll(self, data):
        if self.isEmpty():
            self.emptyMsg()
        else:
            temp = self.head
            while temp:
                temp = temp.next
                self.removeItem(data)