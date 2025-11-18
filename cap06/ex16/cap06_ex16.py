# Capítulo 6 - Exercício 16
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cria uma lista com os valores de índice par
nums_indices_pares = [numeros[i] for i in range(0, len(numeros), 2)]

# Inverte a lista de valores obtida
nums_indices_pares.reverse()

# Substitui os valores de índice par da lista original pelo valor correspondente da lista invertida
for i in range(0, len(numeros), 2):
    numeros[i] = nums_indices_pares.pop(0)

print(numeros)
# Saída: [9, 2, 7, 4, 5, 6, 3, 8, 1, 10]
