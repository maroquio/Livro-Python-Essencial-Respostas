# Capítulo 6 - Exercício 7
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

nomes_notas = {"Pedro": 6.5, "Maria": 8.7, "João": 8.3, "Ana": 7.2}
notas_arredondadas = {nome: round(nota) for nome, nota in nomes_notas.items()}
