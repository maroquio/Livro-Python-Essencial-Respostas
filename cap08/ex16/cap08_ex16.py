# Capítulo 8 - Exercício 16
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimetro(self):
        return self.a + self.b + self.c

class TrianguloRetangulo(Triangulo):
    def __init__(self, a, b):
        super().__init__(a, b, math.sqrt(a**2 + b**2))
    def area(self):
        return 0.5 * self.a * self.b

triangulo = TrianguloRetangulo(3, 4)
print(f"Perímetro: {triangulo.perimetro()}")
print(f"Área: {triangulo.area()}")
