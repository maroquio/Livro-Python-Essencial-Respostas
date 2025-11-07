# Capítulo 4 - Exercício 15
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

# Solução 1
frase = input("Digite uma frase: ")
palavras = frase.split()
frequencia_palavras = {}

for palavra in palavras:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1

for palavra, frequencia in frequencia_palavras.items():
    print(f"A palavra '{palavra}' aparece {frequencia} vez(es) na frase.")

# Solução 2
from collections import Counter

frase = input("Digite uma frase: ")
palavras = frase.split()
contador = Counter(palavras)

for palavra, frequencia in contador.items():
    print(f"A palavra '{palavra}' aparece {frequencia} vez(es)")
