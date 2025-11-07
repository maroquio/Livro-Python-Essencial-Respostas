# Capítulo 4 - Exercício 11
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

frase = input("Digite uma frase: ")

for i in range(0, len(frase), 6):
    print(frase[i:i+6])
