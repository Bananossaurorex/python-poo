import os

os.system("cls || clear") #Limpar Terminal

class Livro:

    def __init__(self,Titulo: str,Autor: str,Numero_Paginas: int,Preco: float) -> None:
    
        self.titulo = Titulo
        self.autor = Autor
        self.numero = Numero_Paginas
        self.preco = Preco

    def exibir_dados(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nNúmero de páginas: {self.numero}\nPreço: {self.preco}"

livro = Livro("O Pé","Marquinzumbunguerqui",345,99.90)
print(livro.exibir_dados())