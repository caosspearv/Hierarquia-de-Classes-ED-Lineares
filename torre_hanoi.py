from linear_structures import SinglyLinkedList

class PilhaCheiaErro(Exception):
    pass

class PilhaVaziaErro(Exception):
    pass

class TipoErro(Exception):
    pass

class Pilha:
    def __init__(self, tipo: str, capacidade: int):
        if tipo not in ('i', 'u'):
            raise TipoErro("Tipo deve ser 'i' para inteiro ou 'u' para caractere")
        self._tipo = tipo
        self._capacidade = capacidade
        self._dados = SinglyLinkedList()  # substitui array por lista encadeada simples
    
    def empilha(self, dado):
        if self.pilha_esta_cheia():
            raise PilhaCheiaErro("A pilha está cheia")
        if self._tipo == 'i' and not isinstance(dado, int):
            raise TipoErro("Dado deve ser inteiro")
        if self._tipo == 'u' and not (isinstance(dado, str) and len(dado) == 1):
            raise TipoErro("Dado deve ser caractere único")
        self._dados.insert_start(dado)
    
    def desempilha(self):
        if self.pilha_esta_vazia():
            raise PilhaVaziaErro("A pilha está vazia")
        topo = self._dados.find_start()
        self._dados.remove_start()
        return topo
    
    def pilha_esta_vazia(self):
        return self._dados.is_empty()
    
    def pilha_esta_cheia(self):
        return self.tamanho() == self._capacidade
    
    def troca(self):
        if self.tamanho() < 2:
            raise PilhaVaziaErro("Não há elementos suficientes para trocar")
        first = self._dados.head
        second = first.next
        first.next = second.next
        second.next = first
        self._dados.head = second
    
    def tamanho(self):
        return self._dados.length()
    
    def __str__(self):
        elementos = []
        current = self._dados.head
        while current:
            elementos.append(str(current.data))
            current = current.next
        elementos.reverse()
        return "[ " + " ".join(elementos) + " ]"


def imprimir_torre_visual(pinos, movimentos, n):
    print(f"\nPosição: {movimentos} passos\n")

    altura = n
    largura_max = n + 2  # largura máxima do disco para alinhamento

    for nivel in range(altura - 1, -1, -1):
        linha = ""
        for pino in pinos:
            if pino.tamanho() > nivel:
                elementos = []
                current = pino._dados.head
                while current:
                    elementos.append(current.data)
                    current = current.next
                elementos.reverse()
                disco = elementos[nivel]
                tam = disco
                lado = "#" * tam
                espaço = " " * (largura_max - tam)
                linha += espaço + lado + "|" + lado + espaço + "   "
            else:
                linha += " " * largura_max + "|" + " " * largura_max + "   "
        print(linha)

    base = ""
    for _ in pinos:
        base += "_" * (largura_max * 2 + 1) + "   "
    print(base)


def torre_de_hanoi(n, origem, destino, auxiliar, pinos, contador, m):
    if n == 1:
        disco = pinos[origem].desempilha()
        pinos[destino].empilha(disco)
        contador[0] += 1

        if contador[0] % m == 0:
            imprimir_torre_visual(pinos, contador[0], sum(p.tamanho() for p in pinos))
            input("Pressione [ENTER] para continuar...")
    else:
        torre_de_hanoi(n-1, origem, auxiliar, destino, pinos, contador, m)
        torre_de_hanoi(1, origem, destino, auxiliar, pinos, contador, m)
        torre_de_hanoi(n-1, auxiliar, destino, origem, pinos, contador, m)


def main():
    n = int(input("Digite o número de discos: "))
    m_str = input("Digite a quantidade de movimentos entre exibições (padrão 1): ")
    m = int(m_str) if m_str.strip() else 1

    pino_inicial = Pilha('i', n)
    pino_intermediario = Pilha('i', n)
    pino_destino = Pilha('i', n)

    for disco in range(n, 0, -1):
        pino_inicial.empilha(disco)

    pinos = [pino_inicial, pino_intermediario, pino_destino]

    print("\nPosição Inicial: 0 passos")
    imprimir_torre_visual(pinos, 0, n)

    contador = [0]  # contador mutável

    torre_de_hanoi(n, 0, 2, 1, pinos, contador, m)

    print(f"\nPosição Final : {contador[0]} passos")
    imprimir_torre_visual(pinos, contador[0], n)


if __name__ == "__main__":
    main()
