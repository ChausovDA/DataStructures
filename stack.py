"""Реализация стека"""


class Node:
    """Объекты стека"""

    def __init__(self, data):
        self.data = data
        self.ref_next = self.ref_prev = None

    def get_data(self):
        """Возвращает данные из объекта"""
        return self.data

    def get_next(self):
        """Возвращает ссылку на следующий объект списка"""
        return self.ref_next

    def set_next(self, new_node):
        """Изменение ссылки на следующий объект списка"""
        self.ref_next = new_node

    def set_prev(self, new_node):
        """Изменение ссылки на предыдущий объект списка"""
        self.ref_prev = new_node


class Stack:
    """Сам стек"""

    def __init__(self):
        self.head = None

    def push(self, new_node):
        """Добавление объекта в стек"""
        if self.head:
            self.head.set_prev(new_node)
        new_node.set_next(self.head)
        new_node.set_prev(None)
        self.head = new_node

    def pop(self):
        """Удаляет и возвращает первый элемент"""
        print(self.head.get_data())
        self.head = self.head.get_next()

    def show(self):
        """Выводит все элементы списка"""
        data = []
        current_node = self.head
        while current_node:
            data.append(current_node.data)
            current_node = current_node.get_next()
        return data


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(Node("1"))
    my_stack.push(Node("2"))
    my_stack.push(Node("3"))
    assert my_stack.show() == ['3', '2', '1']
    my_stack.pop()
    assert my_stack.show() == ['2', '1']
