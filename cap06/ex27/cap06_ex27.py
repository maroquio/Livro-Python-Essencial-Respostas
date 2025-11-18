# Capítulo 6 - Exercício 27
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

generator = fibonacci()
for i in range(20):
    print(next(generator))
