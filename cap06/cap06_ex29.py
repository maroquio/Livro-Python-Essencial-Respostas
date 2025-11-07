# Capítulo 6 - Exercício 29
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

def quadrados(lista):
    for num in lista:
        yield num ** 2

lista = list(range(1, 11))
generator = quadrados(lista)
for quadrado in generator:
    print(quadrado)
