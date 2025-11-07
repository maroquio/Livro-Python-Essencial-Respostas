# Capítulo 1 - Exercício 10
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    raiz = -b / (2 * a)
    print(f"A equação possui uma raiz real: {raiz:.2f}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")
