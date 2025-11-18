# Capítulo 6 - Exercício 15
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_referencia = 5
nova_lista = [num for num in lista_original if num > numero_referencia]
print(nova_lista)
