# Capítulo 6 - Exercício 26
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

def sequencia_infinita():
    num = 1
    while True:
        yield num
        num += 1

generator = sequencia_infinita()
for i in range(10):
    print(next(generator))
