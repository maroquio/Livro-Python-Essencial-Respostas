# Capítulo 3 - Exercício 7
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

soma = 0
cont = 0
num = int(input("Digite um número positivo (ou um negativo para sair): "))
while num >= 0:
    soma += num
    cont += 1
    num = int(input("Digite um número positivo (ou um negativo para sair): "))
media = soma / cont
print(f"A média dos números positivos digitados é {media}")
