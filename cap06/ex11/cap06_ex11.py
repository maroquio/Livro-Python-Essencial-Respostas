# Capítulo 6 - Exercício 11
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

numeros = list(map(int, input("Digite uma lista de números separados por vírgula: ").split(",")))
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)
