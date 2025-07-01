class TaskNode:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, name, priority):
        new_node = TaskNode(name, priority)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_task(self, name):
        current = self.head
        prev = None
        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Задача '{name}' удалена.")
                return
            prev = current
            current = current.next
        print(f"Задача '{name}' не найдена.")

    def print_tasks(self):
        if not self.head:
            print("Список задач пуст.")
            return
        current = self.head
        print("Список задач:")
        while current:
            print(f" - {current.name} (Приоритет: {current.priority})")
            current = current.next

if __name__ == "__main__":
    tasks = TaskList()

    tasks.add_task("Купить продукты", 2)
    tasks.add_task("Позвонить другу", 1)
    tasks.add_task("Прочитать книгу", 3)

    tasks.print_tasks()

    tasks.remove_task("Позвонить другу")

    tasks.print_tasks()
