# Capítulo 2 - Exercício 18
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0 and num4 % 2 == 0 and num5 % 2 == 0:
    print("Todos os números são pares.")
else:
    print("Há pelo menos um número ímpar.")
