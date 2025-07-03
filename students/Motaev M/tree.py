class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()

print("Пустая очередь:", queue.is_empty())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Размер очереди после добавления элементов:", queue.size())

print("Первый элемент (peek):", queue.peek())

print("Удалённый элемент (dequeue):", queue.dequeue())
print("Первый элемент после удаления:", queue.peek())

print("Размер очереди после удаления элемента:", queue.size())

print("Удалённый элемент (dequeue):", queue.dequeue())
print("Удалённый элемент (dequeue):", queue.dequeue())

print("Пустая очередь после удаления всех элементов:", queue.is_empty())

try:
    queue.peek()
except IndexError as e:
    print("Ошибка при вызове peek на пустой очереди:", e)

try:
    queue.dequeue()
except IndexError as e:
    print("Ошибка при вызове dequeue на пустой очереди:", e)
