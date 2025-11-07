# Capítulo 4 - Exercício 21
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import datetime

hora_atual = datetime.datetime.now()
hora_formatada = hora_atual.strftime("%I:%M %p")
print(hora_formatada)
