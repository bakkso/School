class PriorityQueue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self): return len(self.items)
    def clear(self): self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            return highest

    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)

    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]

    def display(self):
        if not self.isEmpty():
            print(self.items)


q = PriorityQueue()

q.enqueue(23)
q.enqueue(28)
q.enqueue(39)
q.enqueue(14)
q.enqueue(55)

q.dequeue()
q.display()

q.dequeue()
q.display()

q.dequeue()
q.display()

q.dequeue()
q.display()

q.dequeue()
q.display()
