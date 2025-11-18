# Capítulo 2 - Exercício 20
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

cpf = input("Digite um número de CPF: ")

if len(cpf) == 11 and cpf.isdigit():
    print("O CPF é válido.")
else:
    print("O CPF é inválido.")
