class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.first = 0
        self.last = 0

    def insert(self, item):
        if self.last < len(self.queue):
            self.queue[self.last] = item
            self.last += 1
        else:
            self.increase_size()
            self.queue[self.last] = item
            self.last += 1

    def pop(self):
        x = self.queue[self.first]
        self.first += 1
        return x

    def increase_size(self):
        new_queue = [None] * len(self.queue) * 2

        for index, item in enumerate(self.queue):
            new_queue[index] = item

        self.queue = new_queue

    def size(self):
        return self.last - self.first

    def front(self):
        return self.queue[self.first]

    def empty(self):
        return self.last == self.first
