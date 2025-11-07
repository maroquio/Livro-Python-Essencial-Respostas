# Capítulo 3 - Exercício 19
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

palavra = input("Digite uma palavra: ")
palavra_invertida = ""

for i in range(len(palavra) - 1, -1, -1):
    palavra_invertida += palavra[i]

if palavra == palavra_invertida:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
