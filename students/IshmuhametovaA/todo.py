class TaskNode:
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority
        self.next = None

    def __str__(self):
        return f"{self.name} (приоритет: {self.priority})"


class TaskList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_task(self, name: str, priority: int) -> None:
        new_task = TaskNode(name, priority)
        
        if self.head is None:
            self.head = new_task
            self.tail = new_task
        else:
            self.tail.next = new_task
            self.tail = new_task

    def remove_task(self, name: str) -> bool:
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

    def print_tasks(self) -> None:
        """Выводит список задач в порядке добавления"""
        if self.head is None:
            print("Список задач пуст")
            return
        
        print("Список задач:")
        current = self.head
        while current is not None:
            print(f"- {current}")
            current = current.next


if __name__ == "__main__":
    todo_list = TaskList()
    
    todo_list.add_task("Купить продукты", 2)
    todo_list.add_task("Сделать дз", 1)
    todo_list.add_task("Позвонить маме", 3)
    todo_list.add_task("Тренировка", 4)
    todo_list.add_task("Искупаться", 5)
    todo_list.add_task("Поспать", 6)

    todo_list.print_tasks()
    
    print("\nУдаляем задачу 'Позвонить маме'")
    if todo_list.remove_task("Позвонить маме"):
        print("Задача успешно удалена")
    else:
        print("Задача не найдена")

    print("\nОбновленный список задач:")
    todo_list.print_tasks()
    
    print("\nПытаемся удалить несуществующую задачу")
    if todo_list.remove_task("Починить компьютер"):
        print("Задача успешно удалена")
    else:
        print("Задача не найдена")
