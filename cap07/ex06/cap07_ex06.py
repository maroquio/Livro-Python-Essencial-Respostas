# Capítulo 7 - Exercício 6
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import shutil
import os

nome_arquivo = input("Digite o nome do arquivo: ")
base = os.path.splitext(nome_arquivo)[0]
shutil.copy2(nome_arquivo, base + ".cópia")
with open(base + ".cópia", "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)
