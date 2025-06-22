from doubly_linked_list_extended import DoublyLinkedListExtended

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
        return self._lista.pop_back()

    def esta_vazia(self):
        return self._lista.is_empty()

    def tamanho(self):
        return self._lista.length()

    def __str__(self):
        return str(self._lista)
