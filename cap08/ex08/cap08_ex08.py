# Capítulo 8 - Exercício 8
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")

# Criando uma instância da classe Aluno
aluno1 = Aluno("João", 20, "20230001")

# Chamando o método mostrar_dados para o aluno
aluno1.mostrar_dados()
