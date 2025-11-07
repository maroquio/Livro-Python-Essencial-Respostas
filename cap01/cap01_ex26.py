# Capítulo 1 - Exercício 26
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math

g = 9.81 
h = float(input("Altitude inicial do objeto em metros: "))
t = math.sqrt((2*h)/g)
print(f"O objeto levará {t:.2f} segundos para atingir o solo.")
