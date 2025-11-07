# Capítulo 4 - Exercício 20
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import datetime

data_atual = datetime.date.today()
data_formatada = data_atual.strftime("%d-%m-%Y")
print(data_formatada)
