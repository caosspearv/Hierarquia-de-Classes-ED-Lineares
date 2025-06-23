import math

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SimpleCircularList:
    def __init__(self, size, iterable=None):
        self.size = size
        self.count = 0
        self.head = None
        self.current = None
        if iterable is not None:
            for item in iterable:
                self.insert(item)

    def insert(self, item):
        if self.count == self.size:
            raise OverflowError("Lista circular cheia")
        new_node = CircularNode(item)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            self.current = new_node
        else:
            new_node.next = self.current.next
            self.current.next = new_node
            self.current = new_node
        self.count += 1

    def remove(self):
        if self.count == 0:
            raise IndexError("Lista circular vazia")
        remove_node = self.current.next
        if remove_node == self.current:
            self.head = None
            self.current = None
        else:
            self.current.next = remove_node.next
            if remove_node == self.head:
                self.head = remove_node.next
        self.count -= 1
        return remove_node.data

    def peek(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bound")
        node = self.head
        for _ in range(index):
            node = node.next
        return node.data

    def swap(self, i):
        if self.count < 2:
            return
        if i < 0 or i >= self.count - 1:
            raise IndexError("Swap index out of bound")
        node = self.head
        for _ in range(i):
            node = node.next
        next_node = node.next
        node.data, next_node.data = next_node.data, node.data

    def bubble_sort(self):
        if self.count < 2:
            return
        for _ in range(self.count):
            swapped = False
            node = self.head
            for _ in range(self.count - 1):
                nxt = node.next
                if node.data > nxt.data:
                    node.data, nxt.data = nxt.data, node.data
                    swapped = True
                node = node.next
            if not swapped:
                break

    def calcular_perimetro(self):
        if self.count < 2:
            return 0.0
        peri = 0.0
        node = self.head
        for _ in range(self.count):
            p1 = node.data
            p2 = node.next.data
            peri += self._distancia(p1, p2)
            node = node.next
        return peri

    @staticmethod
    def _distancia(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        return math.sqrt(dx * dx + dy * dy)

    def __str__(self):
        if self.count == 0:
            return "[]"
        result = []
        node = self.head
        for _ in range(self.count):
            result.append(str(node.data))
            node = node.next
        return "[" + ", ".join(result) + "]"


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __gt__(self, other):
        if self.x == other.x:
            return self.y > other.y
        return self.x > other.x

    def __str__(self):
        return f"({self.x},{self.y})"
