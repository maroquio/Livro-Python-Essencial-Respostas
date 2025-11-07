# Capítulo 3 - Exercício 11
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math

for i in range(1, 101):
    raiz = math.sqrt(i)
    if raiz == int(raiz):
        print(i)
