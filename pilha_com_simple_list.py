from simple_list import SimpleList

class PilhaComSimpleList:
    def __init__(self):
        self._lista = SimpleList()

    def empilha(self, item):
        self._lista.push(item)

    def desempilha(self):
        if self.esta_vazia():
            raise IndexError("Pilha vazia")
        return self._lista.pop()

    def topo(self):
        if self.esta_vazia():
            raise IndexError("Pilha vazia")
        return self._lista.peek(0)

    def esta_vazia(self):
        return self._lista.is_empty()

    def tamanho(self):
        return self._lista.length()

    def __str__(self):
        return str(self._lista)
