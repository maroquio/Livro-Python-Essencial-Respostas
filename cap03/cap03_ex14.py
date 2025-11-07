# Capítulo 3 - Exercício 14
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

num = int(input("Digite um número: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} não é um número primo")
            break
    else:
        print(f"{num} é um número primo")
else:
    print(f"{num} não é um número primo")
