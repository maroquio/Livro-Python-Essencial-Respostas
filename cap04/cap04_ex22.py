# Capítulo 4 - Exercício 22
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime("%A, %d de %B de %Y, %H:%M")

print(data_formatada)
