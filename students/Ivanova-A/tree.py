class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Очередь пуста")
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Очередь пуста")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.peek())  
print(q.size())  

print(q.dequeue())  
print(q.dequeue())  

print(q.is_empty())  

print(q.dequeue()) 
print(q.is_empty()) 
