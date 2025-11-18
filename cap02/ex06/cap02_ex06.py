# Capítulo 2 - Exercício 6
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

texto = input("Digite um texto: ").replace("\ ", "").lower()
texto_invertido = texto[::-1]

if texto == texto_invertido:
    print("O texto é um palíndromo.")
else:
    print("O texto não é um palíndromo.")
