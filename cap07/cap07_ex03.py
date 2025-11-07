# Capítulo 7 - Exercício 3
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

nome_arquivo = input("Digite o nome do arquivo: ")
with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()

linhas_invertidas = [linha[::-1] for linha in linhas]

with open("arquivo_invertido.txt", "w") as arquivo:
    arquivo.writelines(linhas_invertidas)
