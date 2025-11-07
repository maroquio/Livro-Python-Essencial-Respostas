# Capítulo 2 - Exercício 11
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

idade = int(input("Digite sua idade: "))
nacionalidade = input("Digite sua nacionalidade: ")

if idade >= 16 and nacionalidade.lower() == "brasileira":
    print("Você pode votar.")
else:
    print("Você não pode votar.")
