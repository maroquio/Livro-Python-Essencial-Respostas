# Capítulo 7 - Exercício 4
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import os
nome_arquivo = input("Digite o nome do arquivo: ")
base = os.path.splitext(nome_arquivo)[0]
extensao = os.path.splitext(nome_arquivo)[1]
os.rename(nome_arquivo, f"{base}_renomeado{extensao}")
