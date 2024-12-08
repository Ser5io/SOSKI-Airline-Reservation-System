from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.counter = 0
    def isEmpty(self):
        return self.top == None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")
    def getSize(self):
        pass
    def push(self,data):
        self.items.append(data)
    def pop(self):
        pass
    def display(self):
        pass
    def revese(self):
        pass
    def clear(self):
        pass