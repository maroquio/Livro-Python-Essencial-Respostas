# Capítulo 6 - Exercício 14
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

nomes = ["Ana", "João", "Carlos", "Pedro"]
notas = [8.5, 9.0, 7.0, 8.0]

lista_notas = sorted([(nome, nota) for nome, nota in zip(nomes, notas)], key=lambda x: x[1], reverse=True)
