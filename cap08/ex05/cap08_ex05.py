# Capítulo 8 - Exercício 5
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("Som genérico do animal.")

# Criando uma instância da classe Animal
meu_animal = Animal("Cachorro", 3)

# Chamando o método emitir_som para o animal
meu_animal.emitir_som()
