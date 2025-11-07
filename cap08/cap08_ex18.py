# Capítulo 8 - Exercício 18
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som genérico do animal"

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au Au"

cachorro = Cachorro("Totó")
print(cachorro.emitir_som())
