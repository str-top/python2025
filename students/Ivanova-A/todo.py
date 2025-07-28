class TaskNode:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.next = None


class TaskList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_task(self, name, priority):
        new_node = TaskNode(name, priority)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_task(self, name):
        current = self.head
        previous = None
        
        while current:
            if current.name == name:
                if previous:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                else:
                    self.head = current.next
                    if not self.head:
                        self.tail = None
                return True
            previous = current
            current = current.next
        return False

    def print_tasks(self):
        current = self.head
        if not current:
            print("Список задач пуст")
            return
        
        print("Список задач:")
        while current:
            print(f"- {current.name} (приоритет: {current.priority})")
            current = current.next


todo_list = TaskList()

todo_list.add_task("Купить хлеб", 2)
todo_list.add_task("Сделать домашнее задание", 1)
todo_list.add_task("Позвонить маме", 3)

todo_list.print_tasks()

print("\nУдаляем задачу 'Купить хлеб'")
todo_list.remove_task("Купить хлеб")

todo_list.print_tasks()

print("\nДобавляем задачу 'Записаться к врачу'")
todo_list.add_task("Записаться к врачу", 2)

todo_list.print_tasks()
