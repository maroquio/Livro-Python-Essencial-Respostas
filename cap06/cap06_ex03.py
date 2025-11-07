# Capítulo 6 - Exercício 3
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

# Cria uma lista com o quadrado dos números pares entre 0 e 10
quadrados = [x**2 for x in range(11) if x % 2 == 0]

print(quadrados)
