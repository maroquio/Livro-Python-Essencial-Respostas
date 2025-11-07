# Capítulo 6 - Exercício 8
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
quadrados = list(map(lambda n: n**2, numeros))
