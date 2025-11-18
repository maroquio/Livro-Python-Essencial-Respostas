# Capítulo 4 - Exercício 7
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import re

usuario = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")

usuario_limpo = re.sub('\W+','', usuario )
senha_limpa = re.sub('\W+','', senha )

if usuario != usuario_limpo:
    print(f"O nome de usuário foi modificado para: {usuario_limpo}")

if senha != senha_limpa:
    print(f"A senha foi modificada para: {senha_limpa}")
