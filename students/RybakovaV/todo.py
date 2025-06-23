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
      new_task = TaskNode(name, priority)
      if self.head is None:
        self.head = new_task
        self.tail = new_task
      else:
        self.tail.next = new_task
        self.tail = new_task
    def remove_task(self, name):
        current = self.head
        previous = None

        while current is not None:
          if current.name == name:
            if previous is None:
              self.head = current.next
              if self.head is None:
                self.tail = None
            else:
              previous.next = current.next
              if current.next is None:
                self.tail = previous
            return True
          previous = current
          current = current.next
        return False

    def print_tasks(self):
        current = self.head
        if current is None:
          print("Список задач пуст")
          return
        print("Список задач:")
        while current is not None:
          print(f"- {current.name} (приоритет: {current.priority})")
          current = current.next
todo_list = TaskList()
todo_list.add_task("Купить продукты", 2)
todo_list.add_task("Сделать домашнее задание", 1)
todo_list.add_task("Позвонить другу", 3)
todo_list.print_tasks()
todo_list.remove_task("Сделать домашнее задание")
todo_list.print_tasks()
