# Capítulo 6 - Exercício 30
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import random

def leitura_sensor():
    while True:
        yield random.randint(0, 100)

generator = leitura_sensor()
for i in range(10):
    print(next(generator))
