# Capítulo 3 - Exercício 17
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

numeros = []
for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)
maior = segundo_maior = float('-inf')
menor = segundo_menor = float('inf')
for num in numeros:
    if num > maior:
        segundo_maior = maior
        maior = num
    elif num < maior and num > segundo_maior:
        segundo_maior = num
    if num < menor:
        segundo_menor = menor
        menor = num
    elif num > menor and num < segundo_menor:
        segundo_menor = num
print(f"O segundo maior número é {segundo_maior}")
print(f"O segundo menor número é {segundo_menor}")
