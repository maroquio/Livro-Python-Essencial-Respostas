# Capítulo 4 - Exercício 23
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import datetime

data1 = datetime.date(2022, 1, 1)
data2 = datetime.date(2022, 2, 1)

diferenca = data2 - data1

print(diferenca.days)
