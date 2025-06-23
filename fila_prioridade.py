from linear_structures import DoublyLinkedList

class DoublyLinkedListExtended(DoublyLinkedList):
    def __init__(self, iterable=None):
        super().__init__(iterable)
        if iterable is not None:
            self.bubble_sort()

    def push(self, item):
        self.insert_start(item)

    def push_back(self, item):
        self.insert_end(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty list")
        item = self.find_start()
        self.remove_start()
        return item

    def pop_back(self):
        if self.is_empty():
            raise IndexError("Pop back from empty list")
        item = self.find_end()
        self.remove_end()
        return item

    def peek(self, index):
        return self.find_at(index)

    def swap(self, i):
        if i < 0 or i + 1 >= self.length():
            raise IndexError("Swap index out of bound")
        current = self.head
        count = 0
        while current and count < i:
            current = current.next
            count += 1
        if current is None or current.next is None:
            raise IndexError("Swap impossível, posição inválida")
        current.data, current.next.data = current.next.data, current.data

    def bubble_sort(self):
        n = self.length()
        if n < 2:
            return
        for _ in range(n):
            swapped = False
            current = self.head
            while current and current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
            if not swapped:
                break

    def insert_ordered(self, item):
        new_node = self._create_node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        current = self.head
        while current and current.data < item:
            current = current.next
        if current is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        elif current == self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node

    def _create_node(self, item):
        from linear_structures import DoublyLinkedListNode
        return DoublyLinkedListNode(item)


class FilaDePrioridade:
    def __init__(self, iterable=None):
        self._lista = DoublyLinkedListExtended()
        if iterable is not None:
            for item in iterable:
                self._lista.insert_ordered(item)

    def inserir(self, item):
        self._lista.insert_ordered(item)

    def remover_maior_prioridade(self):
        if self.esta_vazia():
            raise IndexError("Fila vazia")
        # maior prioridade no fim da lista ordenada crescente
        return self._lista.pop_back()

    def esta_vazia(self):
        return self._lista.is_empty()

    def tamanho(self):
        return self._lista.length()

    def __str__(self):
        return str(self._lista)
