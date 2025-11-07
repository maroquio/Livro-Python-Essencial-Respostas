# Capítulo 6 - Exercício 22
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import random
letras = 'abcdefghijklmnopqrstuvwxyz'
nome = 'maroquio'
letras_nome = set(nome)
sorteios = 0
letras_sorteadas = ''

while set(letras_sorteadas) != set(letras_nome):
    letra = random.choice(letras)
    if letra in letras_nome and letra not in letras_sorteadas:
        letras_sorteadas += letra
    sorteios += 1

print(nome, letras_sorteadas)
print(sorteios)
