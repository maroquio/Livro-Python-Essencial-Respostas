# Capítulo 3 - Exercício 8
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

num = int(input("Digite um número: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print(f"O fatorial de {num} é {fatorial}")
