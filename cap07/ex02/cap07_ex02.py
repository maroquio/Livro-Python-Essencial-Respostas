# Capítulo 7 - Exercício 2
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

nome_arquivo = input("Digite o nome do arquivo: ")
with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()
print(len(linhas))
