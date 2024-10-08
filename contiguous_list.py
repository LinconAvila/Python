class ContiguousList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.list = [None] * capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def resize(self):
        new_capacity = self.capacity * 2
        new_list = [None] * new_capacity
        for i in range(self.size):
            new_list[i] = self.list[i]
        self.list = new_list
        self.capacity = new_capacity

    def insert(self, element):
        if self.is_full():
            self.resize()
        self.list[self.size] = element
        self.size += 1

    def remove(self, position):
        if self.is_empty():
            raise Exception("List is empty")
        if position < 0 or position >= self.size:
            raise IndexError("Invalid position")
        for i in range(position, self.size - 1):
            self.list[i] = self.list[i + 1]
        self.list[self.size - 1] = None
        self.size -= 1

    def get(self, position):
        if position < 0 or position >= self.size:
            raise IndexError("Invalid position")
        return self.list[position]

    def list_size(self):
        return self.size
