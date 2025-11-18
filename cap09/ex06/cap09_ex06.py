# Capítulo 9 - Exercício 6
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import random

numero_secreto = random.randint(1, 10)

while True:
    try:
        palpite = int(input("Adivinhe um número entre 1 e 10: "))
        if palpite == numero_secreto:
            print("Parabéns, você acertou!")
            break
        else:
            print("Infelizmente você errou, tente novamente.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número.")
