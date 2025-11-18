# Capítulo 4 - Exercício 8
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import re

while True:
    frase = input("Digite uma frase com 5 palavras: ")
    palavras = re.findall(r'\b\w+\b', frase)

    if len(palavras) == 5:
        break
    else:
        print("Erro: a frase deve conter exatamente 5 palavras. Tente novamente.")

for palavra in palavras:
    print(palavra)
