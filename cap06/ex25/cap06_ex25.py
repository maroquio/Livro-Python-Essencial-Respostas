# Capítulo 6 - Exercício 25
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import random

participantes = ['Alice', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena', 'Igor', 'Juliana']
amigo_secreto = {}

for p in participantes:
    possiveis = list(set(participantes) - set([p]) - set(amigo_secreto.values()))
    amigo_secreto[p] = random.choice(possiveis)

for p, a in amigo_secreto.items():
    print(f"{p} tirou {a}")
