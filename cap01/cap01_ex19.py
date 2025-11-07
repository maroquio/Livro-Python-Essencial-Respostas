# Capítulo 1 - Exercício 19
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))

hipotenusa = math.sqrt(lado1 ** 2 + lado2 ** 2)

print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")
