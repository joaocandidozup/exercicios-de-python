from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, salario: float):
        self.__nome = nome
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario: float):
        if novo_salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        self.__salario = novo_salario

    @abstractmethod
    def calcular_bonus(self) -> float:
        pass

