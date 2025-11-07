# Capítulo 6 - Exercício 1
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math

# Cria uma lista com as raízes quadradas dos números pares de 0 a 20
raizes = [math.sqrt(x) for x in range(21) if x % 2 == 0]

print(raizes)
