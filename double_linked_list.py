"""Реализация двусвязного списка"""


class Node:
    """Объекты двусвязанного списка"""
    def __init__(self, data):
        self.data = data
        self.ref_next = self.ref_prev = None

    def get_data(self):
        """Возвращает данные из объекта"""
        return self.data

    def get_next(self):
        """Возвращает ссылку на следующий объект списка"""
        return self.ref_next

    def get_prev(self):
        """Возвращает ссылку на предыдущий объект списка"""
        return self.ref_prev

    def set_data(self, new_node):
        """Изменение данных объекта списка"""
        self.data = new_node

    def set_next(self, new_node):
        """Изменение ссылки на следующий объект списка"""
        self.ref_next = new_node

    def set_prev(self, new_node):
        """Изменение ссылки на предыдущий объект списка"""
        self.ref_prev = new_node


class DoubleLinkedList:
    """Сам двусвязный список"""
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, new_node):
        """Добавление элемента в начало списка"""
        if self.head:
            self.head.set_prev(new_node)
        new_node.set_next(self.head)
        new_node.set_prev(None)
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def push_back(self, new_node):
        """Добавление элемента в конец списка"""
        if self.tail:
            self.tail.set_next(new_node)
        new_node.set_prev(self.tail)
        new_node.set_next(None)
        self.tail = new_node
        if not self.head:
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

            if count == index:
                left = current_node.get_prev()
                right = left.get_next()

                left.set_next(new_node)
                new_node.set_prev(left)
                right.set_prev(new_node)
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

            if count == index:
                left = current_node.get_prev()
                right = current_node.get_next()
                left.set_next(right)
                right.set_prev(left)
                return

    def pop_front(self):
        """Удаление первого элемента списка"""
        self.head = self.head.get_next()
        self.head.set_prev(None)

    def pop_back(self):
        """Удаление последнего элемента списка"""
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)

    def show(self):
        """Выводит все элементы списка"""
        data = []
        current_node = self.head
        while current_node:
            data.append(current_node.data)
            current_node = current_node.get_next()
        return data


if __name__ == '__main__':
    my_list = DoubleLinkedList()
    top = Node("Head_node")
    last = Node("Last_node")
    my_list.push_front(top)
    my_list.push_back(last)
    assert my_list.show() == ['Head_node', 'Last_node']
    assert my_list.head == top
    assert my_list.tail == last
    my_list.insert(Node("Node_2"), 1)
    my_list.insert(Node("Node_3"), 2)
    my_list.insert(Node("Node_4"), 3)
    assert my_list.show() == ['Head_node', 'Node_2', 'Node_3', 'Node_4', 'Last_node']
    my_list.erase(3)
    assert my_list.show() == ['Head_node', 'Node_2', 'Node_3', 'Last_node']
    my_list.pop_front()
    my_list.pop_back()
    assert my_list.show() == ['Node_2', 'Node_3']
