class Queue:
    def __init__(self):
        self.items = []  

    def enqueue(self, item):
        self.items.append(item)
        print(f"Добавлен элемент: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста, невозможно удалить элемент")
            return None
        item = self.items.pop(0)
        print(f"Удален элемент: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        item = self.items[0]
        print(f"Первый элемент: {item}")
        return item

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Текущая очередь: {self.items}"


if __name__ == "__main__":
    q = Queue()
    
    print("\n=== Тестирование операций с очередью ===")
    
    print(q)
    print("Очередь пуста?", q.is_empty())
    print("Размер очереди:", q.size())
    q.peek()
    q.dequeue()
    
    print("\nДобавляем элементы:")
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(70)
    print(q)
    print("Очередь пуста?", q.is_empty())
    print("Размер очереди:", q.size())
    
    print("\nПросмотр первого элемента:")
    q.peek()
    print(q)
    
    print("\nУдаляем элементы:")
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    
    print("\nПроверка пустой очереди:")
    print("Очередь пуста?", q.is_empty())
    print("Размер очереди:", q.size())
    q.peek()
    q.dequeue()
