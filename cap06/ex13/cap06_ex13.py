# Capítulo 6 - Exercício 13
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

medias = [(a+b)/2 for a, b in zip(lista1, lista2)]
print(medias)
