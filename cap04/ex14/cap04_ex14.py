# Capítulo 4 - Exercício 14
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

frase = input("Digite uma frase: ")
palavras = frase.split()

for palavra in palavras:
    posicao_inicial = frase.find(palavra)
    print(f"A palavra '{palavra}' começa na posição {posicao_inicial}")
