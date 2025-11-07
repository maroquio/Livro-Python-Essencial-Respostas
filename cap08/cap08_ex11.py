# Capítulo 8 - Exercício 11
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def aumentar_salario(self, aumento):
        self.salario += self.salario * aumento / 100

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Salário: {self.salario}")

# Criação de uma instância da classe Funcionario
funcionario = Funcionario("Maria", 30, 3000)
funcionario.aumentar_salario(10)
funcionario.mostrar_dados()
