# Capítulo 6 - Exercício 5
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

nomes_notas = {"Pedro": 6, "Maria": 9, "João": 8, "Ana": 7}
aprovados = {nome: nota for nome, nota in nomes_notas.items() if nota >= 7}
