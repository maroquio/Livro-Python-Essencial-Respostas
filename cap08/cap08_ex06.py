# Capítulo 8 - Exercício 6
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio**2

# Criando uma instância da classe Circulo
meu_circulo = Circulo(5)

# Chamando o método area para calcular a área do círculo
resultado_area = meu_circulo.area()
print(f"A área do círculo é: {resultado_area}")
