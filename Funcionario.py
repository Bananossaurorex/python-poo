from abc import ABC,abstractmethod
import os

class Funcionario(ABC):
    # Construtor
    def __init__(self,nome: str,telefone: int,email: str,endereco: int,salario_final: float) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        Endedereco = endereco
        self.salario_final = salario_final

    class Medico(Funcionario):
        def __init__(self, nome: str, telefone: int, email: float, endereco: str,salario_final: float) -> None:
