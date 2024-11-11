class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None: 
            self.rear = None
        return dequeued_value

    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

    def destroy(self):
        self.front = None
        self.rear = None
