# Capítulo 2 - Exercício 15
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

palavra = input("Insira uma palavra: ")
primeira_letra = palavra[0].lower()
if primeira_letra in 'aeiou':
    print(f"A palavra '{palavra}' começa com uma vogal.")
else:
    print(f"A palavra '{palavra}' começa com uma consoante.")
