import os

os.system("cls || clear ") # Limpar terminal.

class Endereco:
    def __init__(self, logadouro: str, numero: int,) -> None:
        self.logadouro = logadouro
        self.numero = numero

    def __str__(self) -> str: 
        return f"Logadouro: {self.logadouro}\nNúmero: {self.numero}" 



class Aluno:
    # nome, idade

    #Construtor.
    def __init__(self,nome: str,idade: int, endereco: Endereco) -> None:

        #Atributos
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nIdade: {self.idade}\nEndereco:{self.endereco}" 
        


# Instanciar classe.
aluno = Aluno("Marta",22, Endereco("Rua maluca", 22))
aluno2 = Aluno("Marto",12, Endereco("Rua Sã",66))
#print(f"Nome:  {aluno.nome}")
#print(f"Idade:  {aluno.idade}")
print(aluno)
print(aluno2)

