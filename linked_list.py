"""Реализация связанного списка"""


class Node:
    """Объекты связанного списка"""
    def __init__(self, data):
        self.data = data
        self.ref_next = None

    def get_data(self):
        """Возвращает данные из объекта"""
        return self.data

    def get_next(self):
        """Возвращает ссылку на следующий объект списка"""
        return self.ref_next

    def set_data(self, new_node):
        """Изменение данных объекта списка"""
        self.data = new_node

    def set_next(self, new_node):
        """Изменение ссылки на следующий объект списка"""
        self.ref_next = new_node


class LinkedList:
    """Сам связанный список"""
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, new_node):
        """Добавление элемента в начало списка"""
        new_node.set_next(self.head)
        self.head = new_node

    def push_back(self, new_node):
        """Добавление элемента в конец списка"""
        if self.tail:
            self.tail.set_next(new_node)
        self.tail = new_node

        if self.head is None:
            self.head = new_node

    def insert(self, new_node, index):
        """Добавление нового элемента по индексу"""
        current_node = self.head
        count = 0
        while current_node.get_next() is not None:
            if index == 0:
                self.push_front(new_node)
                return

            count += 1
            current_node = current_node.get_next()

            if count + 1 == index:
                right = current_node.get_next()
                current_node.set_next(new_node)
                new_node.set_next(right)
                return

    def erase(self, index):
        """Удаление элемента по индексу"""
        current_node = self.head
        count = 0
        while current_node.get_next() is not None:
            if index == 0:
                self.pop_front()
                return

            count += 1
            current_node = current_node.get_next()

            if count + 1 == index:
                node_to_remove = current_node.get_next()
                left = node_to_remove.get_next()
                current_node.set_next(left)
                return

    def pop_front(self):
        """Удаление первого элемента списка"""
        self.head = self.head.get_next()

    def pop_back(self):
        """Удаление последнего элемента списка"""
        current_node = self.head
        while current_node.get_next().get_next():
            current_node = current_node.get_next()
        current_node.set_next(None)

    def show(self):
        """Выводит все элементы списка"""
        data = []
        current_node = self.head
        while current_node:
            data.append(current_node.data)
            current_node = current_node.get_next()
        return data


if __name__ == '__main__':
    my_list = LinkedList()

    last = Node("Last_node")
    my_list.push_back(Node("Node_4"))
    my_list.push_back(last)
    assert my_list.show() == ['Node_4', 'Last_node']
    top = Node("Head_node")
    my_list.push_front(Node("Node_3"))
    my_list.push_front(Node("Node_2"))
    my_list.push_front(top)
    assert my_list.show() == ['Head_node', 'Node_2', 'Node_3', 'Node_4', 'Last_node']
    assert my_list.head == top
    assert my_list.tail == last
    my_list.insert(Node("Insert_node"), 3)
    assert my_list.show() == ['Head_node', 'Node_2', 'Node_3', 'Insert_node', 'Node_4', 'Last_node']
    my_list.erase(3)
    assert my_list.show() == ['Head_node', 'Node_2', 'Node_3', 'Node_4', 'Last_node']
    my_list.pop_back()
    assert my_list.show() == ['Head_node', 'Node_2', 'Node_3', 'Node_4']
    my_list.pop_front()
    assert my_list.show() == ['Node_2', 'Node_3', 'Node_4']
