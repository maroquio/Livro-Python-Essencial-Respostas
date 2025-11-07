# Capítulo 8 - Exercício 10
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade)
        self.endereco = endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}")

# Criação de uma instância da classe Cliente
cliente = Cliente("João", 25, "Rua das Flores, 123")
cliente.mostrar_dados()
