# Capítulo 3 - Exercício 16
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

numeros = []
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"O maior número digitado foi {maior}")
print(f"O menor número digitado foi {menor}")
