# Capítulo 4 - Exercício 18
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

from datetime import datetime as dt

hora_atual = dt.now().time()
print(hora_atual.strftime("%H:%M:%S"))
