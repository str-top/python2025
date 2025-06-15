
class TaskNode:
    def __init__(self, name, priority):
        self.name = name 
        self.priority = priority 
        self.next = None  

class TaskList:
    def __init__(self):
        self.head = None  



    def add_task(self, name, priority):
        new_node = Node(name, priority)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove_task(self, name):
        current_node = self.head
        
        
        if current_node and current_node.name == name:
            self.head = current_node.next
            current_node = None
            return
        
        # Поиск узла для удаления
        prev_node = None
        while current_node and current_node.name != name:
            prev_node = current_node
            current_node = current_node.next
        
        # Если узел не найден
        if current_node is None:
            return
        
        # Удаление узла
        prev_node.next = current_node.next
        current_node = None

    def print_tasks(self):
        current_node = self.head
        while current_node:
            print(f'Задача: {current_node.name}  с приоритетом: {current_node.priority}, ')
            current_node = current_node.next
        print("None")
        
to_do_list = TaskList() 
to_do_list.add_task('Убраться',2)
to_do_list.add_task('Приготовить',1)
to_do_list.add_task('Сделать дз',3)
to_do_list.add_task('Пробежка', 4)
to_do_list.print_tasks()
to_do_list.remove_task('Убратьсяяяяяяяяяяяяяяяяяяяя')
to_do_list.print_tasks()
