"""Реализация очереди"""


class Node:
    """Объекты очереди"""

    def __init__(self, data):
        self.data = data
        self.ref_next = self.ref_prev = None

    def get_data(self):
        """Возвращает данные из объекта"""
        return self.data

    def get_next(self):
        """Возвращает ссылку на следующий объект"""
        return self.ref_next

    def get_prev(self):
        """Возвращает ссылку на предыдущий объект"""
        return self.ref_prev

    def set_next(self, new_node):
        """Изменение ссылки на следующий объект"""
        self.ref_next = new_node

    def set_prev(self, new_node):
        """Изменение ссылки на предыдущий объект"""
        self.ref_prev = new_node


class Queue:
    """Сама очередь"""

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, new_node):
        """Добавление объекта в очередь"""
        if self.head:
            self.head.set_prev(new_node)
        new_node.set_next(self.head)
        new_node.set_prev(None)
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def pop(self):
        """Удаляет и возвращает последний элемент"""
        print(self.tail.get_data())
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)

    def show(self):
        """Выводит все объекты очереди"""
        data = []
        current_node = self.head
        while current_node:
            data.append(current_node.data)
            current_node = current_node.get_next()
        return data


if __name__ == '__main__':
    my_queue = Queue()
    my_queue.push(Node("1"))
    my_queue.push(Node("2"))
    my_queue.push(Node("3"))
    assert my_queue.show() == ['3', '2', '1']
    my_queue.pop()
    assert my_queue.show() == ['3', '2']
