# Capítulo 2 - Exercício 13
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 % num2 == 0:
    print(f"{num1} é divisível por {num2}.")
else:
    print(f"{num1} não é divisível por {num2}.")
