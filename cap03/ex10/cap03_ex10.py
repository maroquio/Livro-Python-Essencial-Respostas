# Capítulo 3 - Exercício 10
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

for num in range(1, 101):
    if num > 1:  # os números primos são maiores que 1
        for i in range(2, num):
            if (num % i) == 0:  # se o número é divisível por i, não é primo
                break
        else:  # se o laço não foi interrompido, o número é primo
            print(num)
