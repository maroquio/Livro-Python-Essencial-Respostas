# Capítulo 1 - Exercício 11
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * raio ** 2
comprimento = 2 * math.pi * raio

print(f"Área do círculo: {area:.2f}")
print(f"Comprimento do círculo: {comprimento:.2f}")
