# Capítulo 6 - Exercício 9
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")
nomes_upper = list(map(str.upper, nomes))
print(nomes_upper)
