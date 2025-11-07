# Capítulo 2 - Exercício 19
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import random

numero_aleatorio = random.randint(1, 10)
tentativa = int(input("Tente adivinhar o número entre 1 e 10: "))

if tentativa == numero_aleatorio:
    print("Parabéns, você acertou!")
elif tentativa > numero_aleatorio:
    print("O número é menor.")
else:
    print("O número é maior.")
