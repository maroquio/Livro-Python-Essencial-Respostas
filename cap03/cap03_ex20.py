# Capítulo 3 - Exercício 20
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

n = int(input("Digite um número: "))
for i in range(1, n + 1):
    fatorial = 1
    for j in range(1, i + 1):
        fatorial *= j
    print(f"Fatorial de {i} é {fatorial}")
