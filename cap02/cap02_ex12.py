# Capítulo 2 - Exercício 12
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero (M: masculino, F: feminino): ")

if (genero.upper() == "F"\ and idade >= 60) or (genero.upper() == "M"\ and idade >= 65):
    print("Elegível para aposentadoria.")
else:
    print("Não elegível para aposentadoria.")
