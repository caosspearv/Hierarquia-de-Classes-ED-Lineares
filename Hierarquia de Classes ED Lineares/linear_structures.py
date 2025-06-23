from abc import ABC, abstractmethod
import math

class LinearDataStructure(ABC):
    def __init__(self, iterable=None):
        self.data = []
        if iterable is not None:
            for item in iterable:
                self.data.append(item)

    def length(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def is_full(self):
        return False

    @abstractmethod
    def insert_start(self, item):
        pass

    @abstractmethod
    def insert_end(self, item):
        pass

    @abstractmethod
    def insert_at(self, index, item):
        pass

    @abstractmethod
    def insert_before_key(self, key, item):
        pass

    @abstractmethod
    def insert_after_key(self, key, item):
        pass

    @abstractmethod
    def update_key(self, key, new_item):
        pass

    @abstractmethod
    def update_at(self, index, new_item):
        pass

    @abstractmethod
    def remove_start(self):
        pass

    @abstractmethod
    def remove_end(self):
        pass

    @abstractmethod
    def remove_at(self, index):
        pass

    @abstractmethod
    def remove_key(self, key):
        pass

    @abstractmethod
    def find_start(self):
        pass

    @abstractmethod
    def find_end(self):
        pass

    @abstractmethod
    def find_at(self, index):
        pass

    @abstractmethod
    def find_key(self, key):
        pass

    @abstractmethod
    def find_next_key(self, key):
        pass


class IndexedArray(LinearDataStructure):
    def __init__(self, iterable=None, capacity=4):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.insert_end(item)

    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def insert_start(self, item):
        self.insert_at(0, item)

    def insert_end(self, item):
        if self.is_full():
            self._resize(self.capacity * 2)
        self.data[self.size] = item
        self.size += 1

    def insert_at(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError('Index out of bound')
        if self.is_full():
            self._resize(self.capacity * 2)
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = item
        self.size += 1

    def insert_before_key(self, key, item):
        try:
            idx = self.find_index_of_key(key)
            self.insert_at(idx, item)
        except ValueError:
            self.insert_end(item)

    def insert_after_key(self, key, item):
        try:
            idx = self.find_index_of_key(key)
            self.insert_at(idx + 1, item)
        except ValueError:
            self.insert_end(item)

    def update_key(self, key, new_item):
        idx = self.find_index_of_key(key)
        self.data[idx] = new_item

    def update_at(self, index, new_item):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of bound')
        self.data[index] = new_item

    def remove_start(self):
        if self.is_empty():
            raise IndexError('Array underflow')
        return self.remove_at(0)

    def remove_end(self):
        if self.is_empty():
            raise IndexError('Array underflow')
        item = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return item

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of bound')
        item = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return item

    def remove_key(self, key):
        try:
            idx = self.find_index_of_key(key)
            self.remove_at(idx)
        except ValueError:
            pass

    def find_start(self):
        if self.is_empty():
            raise IndexError('Array underflow')
        return self.data[0]

    def find_end(self):
        if self.is_empty():
            raise IndexError('Array underflow')
        return self.data[self.size - 1]

    def find_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of bound')
        return self.data[index]

    def find_key(self, key):
        idx = self.find_index_of_key(key)
        return self.data[idx]

    def find_next_key(self, key):
        idx = self.find_index_of_key(key)
        for i in range(idx + 1, self.size):
            if self.data[i] == key:
                return self.data[i]
        raise ValueError('No next item with the key')

    def find_index_of_key(self, key):
        for i in range(self.size):
            if self.data[i] == key:
                return i
        raise ValueError('Key not found')

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError('Index out of bound')
        return self.data[index]

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        if index < 0:
            index += self.size
        if index == self.size:
            self.insert_end(value)
            return
        if index < 0 or index > self.size:
            raise IndexError('Index out of bound')
        self.data[index] = value


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(LinearDataStructure):
    def __init__(self, iterable=None):
        super().__init__()
        self.head = None
        if iterable is not None:
            for item in iterable:
                self.insert_end(item)

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def insert_start(self, item):
        new_node = SinglyLinkedListNode(item)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, item):
        new_node = SinglyLinkedListNode(item)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at(self, index, item):
        if index < 0:
            raise IndexError('Index out of bound')
        if index == 0:
            self.insert_start(item)
            return
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if current is None:
            raise IndexError('Index out of bound')
        new_node = SinglyLinkedListNode(item)
        new_node.next = current.next
        current.next = new_node

    def insert_before_key(self, key, item):
        if self.head is None:
            self.insert_end(item)
            return
        if self.head.data == key:
            self.insert_start(item)
            return
        current = self.head
        while current.next and current.next.data != key:
            current = current.next
        if current.next is None:
            self.insert_end(item)
        else:
            new_node = SinglyLinkedListNode(item)
            new_node.next = current.next
            current.next = new_node

    def insert_after_key(self, key, item):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            self.insert_end(item)
        else:
            new_node = SinglyLinkedListNode(item)
            new_node.next = current.next
            current.next = new_node

    def update_key(self, key, new_item):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            raise ValueError('Key not found')
        current.data = new_item

    def update_at(self, index, new_item):
        if index < 0:
            raise IndexError('Index out of bound')
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        if current is None:
            raise IndexError('Index out of bound')
        current.data = new_item

    def remove_start(self):
        if self.head is None:
            raise IndexError('List underflow')
        self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            raise IndexError('List underflow')
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def remove_at(self, index):
        if index < 0:
            raise IndexError('Index out of bound')
        if index == 0:
            self.remove_start()
            return
        current = self.head
        count = 0
        while current.next and count < index - 1:
            current = current.next
            count += 1
        if current.next is None:
            raise IndexError('Index out of bound')
        current.next = current.next.next

    def remove_key(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != key:
            current = current.next
        if current.next is None:
            return
        current.next = current.next.next

    def find_start(self):
        if self.head is None:
            raise IndexError('List underflow')
        return self.head.data

    def find_end(self):
        if self.head is None:
            raise IndexError('List underflow')
        current = self.head
        while current.next:
            current = current.next
        return current.data

    def find_at(self, index):
        if index < 0:
            raise IndexError('Index out of bound')
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        if current is None:
            raise IndexError('Index out of bound')
        return current.data

    def find_key(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            raise ValueError('Key not found')
        return current.data

    def find_next_key(self, key):
        current = self.head
        found = False
        while current:
            if found and current.data == key:
                return current.data
            if current.data == key:
                found = True
            current = current.next
        raise ValueError('No next item with the key')


class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(LinearDataStructure):
    def __init__(self, iterable=None):
        super().__init__()
        self.head = None
        self.tail = None
        if iterable is not None:
            for item in iterable:
                self.insert_end(item)

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def insert_start(self, item):
        new_node = DoublyLinkedListNode(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, item):
        new_node = DoublyLinkedListNode(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_at(self, index, item):
        if index < 0:
            raise IndexError('Index out of bound')
        if index == 0:
            self.insert_start(item)
            return
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        if current is None:
            self.insert_end(item)
            return
        new_node = DoublyLinkedListNode(item)
        new_node.next = current
        new_node.prev = current.prev
        if current.prev:
            current.prev.next = new_node
        current.prev = new_node
        if index == 0:
            self.head = new_node

    def insert_before_key(self, key, item):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            self.insert_end(item)
        else:
            new_node = DoublyLinkedListNode(item)
            new_node.next = current
            new_node.prev = current.prev
            if current.prev:
                current.prev.next = new_node
            else:
                self.head = new_node
            current.prev = new_node

    def insert_after_key(self, key, item):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            self.insert_end(item)
        else:
            new_node = DoublyLinkedListNode(item)
            new_node.prev = current
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            else:
                self.tail = new_node
            current.next = new_node

    def update_key(self, key, new_item):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            raise ValueError('Key not found')
        current.data = new_item

    def update_at(self, index, new_item):
        if index < 0:
            raise IndexError('Index out of bound')
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        if current is None:
            raise IndexError('Index out of bound')
        current.data = new_item

    def remove_start(self):
        if self.head is None:
            raise IndexError('List underflow')
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def remove_end(self):
        if self.tail is None:
            raise IndexError('List underflow')
        if self.tail.prev is None:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def remove_at(self, index):
        if index < 0:
            raise IndexError('Index out of bound')
        if index == 0:
            self.remove_start()
            return
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        if current is None:
            raise IndexError('Index out of bound')
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.tail:
            self.tail = current.prev

    def remove_key(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            return
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

    def find_start(self):
        if self.head is None:
            raise IndexError('List underflow')
        return self.head.data

    def find_end(self):
        if self.tail is None:
            raise IndexError('List underflow')
        return self.tail.data

    def find_at(self, index):
        if index < 0:
            raise IndexError('Index out of bound')
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        if current is None:
            raise IndexError('Index out of bound')
        return current.data

    def find_key(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            raise ValueError('Key not found')
        return current.data

    def find_next_key(self, key):
        current = self.head
        found = False
        while current:
            if found and current.data == key:
                return current.data
            if current.data == key:
                found = True
            current = current.next
        raise ValueError('No next item with the key')
