from linear_structures_full import IndexedArray

class SimpleList:
    def __init__(self, iterable=None):
        self._array = IndexedArray()
        if iterable is not None:
            for item in iterable:
                self._array.insert_end(item)

    def push(self, item):
        self._array.insert_start(item)

    def pop(self):
        if self._array.is_empty():
            raise IndexError("Pop from empty list")
        return self._array.remove_start()

    def peek(self, index):
        return self._array.find_at(index)

    def length(self):
        return self._array.length()

    def is_empty(self):
        return self._array.is_empty()

    def __str__(self):
        return str([self._array[i] for i in range(self.length())])
