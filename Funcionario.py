from abc import ABC,abstractmethod
import os
os.system("clear")

class Endereco:
    def __init__(self, logadouro: str, numero: int,) -> None:
        self.logadouro = logadouro
        self.numero = numero
    def __str__(self) -> str: 
        return f"Logadouro: {self.logadouro}\nNúmero: {self.numero}" 

class Funcionario(ABC):
    # Construtor
    def __init__(self,nome: str,telefone: int,email: str,endereco: Endereco,salario_final: float) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        Endedereco = endereco
        self.salario_final = salario_final

class Medico(Funcionario):
    def __str__(self) -> str:
        return f"Nome:{self.nome}\nTelefone: {self.telefone}"

medico1=Medico("Pedro",12345678,"pedrinhodelas@gmail.com",Endereco("Rua do Pedrin",23),10000)
#print(medico1.nome)
print(medico1)