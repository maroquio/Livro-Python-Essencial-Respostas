# Capítulo 4 - Exercício 9
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import re

cpf = input("Digite um CPF no formato 999.999.999-99: ")
padrao_cpf = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

if re.fullmatch(padrao_cpf, cpf):
    print("CPF no formato correto.")
else:
    print("CPF em formato incorreto.")
