from abc import ABC, abstractmethod
from typing import List
import copy
from linear_structures import IndexedArray

class MatrizABC(ABC):
    def __init__(self, linhas: int, colunas: int, nome: str):
        self.linhas = linhas
        self.colunas = colunas
        self.nome = nome

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def sub(self, other):
        pass

    @abstractmethod
    def mul(self, other):
        pass

    @abstractmethod
    def transposta(self):
        pass

    @abstractmethod
    def imprimir(self):
        pass

    def ehquadrada(self):
        return self.linhas == self.colunas

    def tipo(self):
        return self.__class__.__name__

    def tra(self):
        raise NotImplementedError("Traço só para matrizes quadradas")

    def determinante(self):
        raise NotImplementedError("Determinante só para matrizes triangulares")

    @abstractmethod
    def getelemento(self, i, j):
        pass


class MatrizGeral(MatrizABC):
    def __init__(self, linhas: int, colunas: int, dados: List[List[float]] = None, nome: str = ""):
        super().__init__(linhas, colunas, nome)
        if dados:
            self.dados = IndexedArray()
            for linha in dados:
                arr_linha = IndexedArray()
                for x in linha:
                    arr_linha.insert_end(x)
                self.dados.insert_end(arr_linha)
        else:
            self.dados = IndexedArray()
            for _ in range(linhas):
                linha = IndexedArray()
                for _ in range(colunas):
                    linha.insert_end(0.0)
                self.dados.insert_end(linha)

    def add(self, other):
        if not isinstance(other, MatrizABC):
            raise TypeError("Operação somente entre matrizes")
        if self.linhas != other.linhas or self.colunas != other.colunas:
            raise ValueError("Dimensões incompatíveis para soma")
        if type(self) == type(other):
            return self._soma_especializada(other)
        resultado = MatrizGeral(self.linhas, self.colunas)
        for i in range(self.linhas):
            for j in range(self.colunas):
                resultado.dados[i][j] = self.dados[i][j] + other.getelemento(i, j)
        return resultado

    def _soma_especializada(self, other):
        resultado = MatrizGeral(self.linhas, self.colunas)
        for i in range(self.linhas):
            for j in range(self.colunas):
                resultado.dados[i][j] = self.dados[i][j] + other.dados[i][j]
        return resultado

    def sub(self, other):
        if self.linhas != other.linhas or self.colunas != other.colunas:
            raise ValueError("Dimensões incompatíveis para subtração")
        resultado = MatrizGeral(self.linhas, self.colunas)
        for i in range(self.linhas):
            for j in range(self.colunas):
                resultado.dados[i][j] = self.dados[i][j] - other.getelemento(i, j)
        return resultado

    def mul(self, other):
        if isinstance(other, (int, float)):
            resultado = MatrizGeral(self.linhas, self.colunas)
            for i in range(self.linhas):
                for j in range(self.colunas):
                    resultado.dados[i][j] = self.dados[i][j] * other
            return resultado
        elif isinstance(other, MatrizABC):
            if self.colunas != other.linhas:
                raise ValueError("Dimensões incompatíveis para multiplicação")
            resultado = MatrizGeral(self.linhas, other.colunas)
            for i in range(self.linhas):
                for j in range(other.colunas):
                    soma = 0.0
                    for k in range(self.colunas):
                        soma += self.dados[i][k] * other.getelemento(k, j)
                    resultado.dados[i][j] = soma
            return resultado
        else:
            raise TypeError("Multiplicação inválida")

    def transposta(self):
        resultado = MatrizGeral(self.colunas, self.linhas)
        for i in range(self.linhas):
            for j in range(self.colunas):
                resultado.dados[j][i] = self.dados[i][j]
        return resultado

    def getelemento(self, i, j):
        return self.dados[i][j]

    def imprimir(self):
        print(f"Matriz {self.nome} - {self.tipo()} {self.linhas}x{self.colunas}")
        for i in range(self.linhas):
            linha = []
            for j in range(self.colunas):
                linha.append(f"{self.dados[i][j]:.2f}")
            print(" ".join(linha))

# As outras classes (MatrizDiagonal, MatrizTriangularInferior, MatrizTriangularSuperior)
# podem ser adaptadas do mesmo modo, usando IndexedArray para dados internos.

# A classe CalculadoraMatricial também deve usar essas classes para manter a compatibilidade.

# Se desejar, posso adaptar o código completo da calculadora para você.
