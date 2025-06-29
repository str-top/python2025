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
print("Создаем очередь и добавляем элементы:")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(f"Очередь: {q.items}")
print(f"Размер очереди: {q.size()}")
print(f"Первый элемент (peek): {q.peek()}")
    
print("\nУдаляем элементы из очереди:")
print(f"dequeue: {q.dequeue()}")
print(f"Очередь после dequeue: {q.items}")
print(f"dequeue: {q.dequeue()}")
print(f"Очередь после dequeue: {q.items}")
    
print("\nПроверяем состояние очереди:")
print(f"Очередь пуста? {q.is_empty()}")
print(f"Очередь: {q.items}")
print(f"dequeue: {q.dequeue()}")
print(f"Очередь пуста? {q.is_empty()}")
    
print("\nПопытка dequeue из пустой очереди:")
try:
  q.dequeue()
except IndexError as e:
  print(f"Ошибка: {e}")
