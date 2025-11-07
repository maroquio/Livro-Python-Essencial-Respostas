# Capítulo 4 - Exercício 2
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import math
import locale

# Configura para o formato de moeda brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

numero = float(input("Insira um número: "))
raiz = math.sqrt(numero)

# Formata para moeda brasileira
valor_monetario = locale.currency(raiz, grouping=True)

print("A raiz quadrada do número informado é:", valor_monetario)
