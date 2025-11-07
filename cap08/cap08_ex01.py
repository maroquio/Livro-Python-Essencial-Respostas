# Capítulo 8 - Exercício 1
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Criando instâncias da classe Pessoa
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

# Chamando o método mostrar_dados para cada instância
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()
