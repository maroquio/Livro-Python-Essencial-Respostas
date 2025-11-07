# Capítulo 1 - Exercício 18
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math

angulo_radianos = float(input("Digite o valor do ângulo em radianos: "))

angulo_graus = angulo_radianos * 180 / math.pi

print(f"O ângulo em graus é: {angulo_graus:.2f}°")
