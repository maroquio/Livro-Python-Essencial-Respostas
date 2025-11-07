# Capítulo 8 - Exercício 7
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

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Salário: R${self.salario:.2f}")

# Criando uma lista com pessoas e funcionários
pessoas_e_funcionarios = [
    Pessoa("João", 30),
    Pessoa("Maria", 25),
    Funcionario("Carlos", 40, 3000),
    Funcionario("Ana", 35, 2500)
]

# Chamando o método mostrar_dados para cada objeto da lista
for pessoa_ou_funcionario in pessoas_e_funcionarios:
    pessoa_ou_funcionario.mostrar_dados()
