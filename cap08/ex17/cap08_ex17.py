# Capítulo 8 - Exercício 17
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

class Cilindro(Circulo):
    def __init__(self, raio, altura):
        super().__init__(raio)
        self.altura = altura

    def volume(self):
        return self.area() * self.altura

cilindro = Cilindro(3, 5)
print(cilindro.area())
print(cilindro.volume())
