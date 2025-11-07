# Capítulo 6 - Exercício 4
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

# Cria uma lista com os números divisíveis por 3 ou 5 de 0 a 30
divisiveis = [x for x in range(31) if x % 3 == 0 or x % 5 == 0]

print(divisiveis)
