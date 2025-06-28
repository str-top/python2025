class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    
    def peek(self):
        return self.items[0]
    
    def is_empty(self):
        if len(self.items) == 0:
            print('очередь пуста')
        else:
            print(f'в очереди {len(self.items)} элемента(ов)')
    
    def size(self):
        return len(self.items)
    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.size())
print(q.dequeue())
print(q.peek())
q.is_empty()
    
