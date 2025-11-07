# Capítulo 4 - Exercício 24
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import datetime

hora1 = datetime.datetime.strptime("08:00", "%H:%M")
hora2 = datetime.datetime.strptime("15:00", "%H:%M")

diferenca = hora2 - hora1

print(diferenca.seconds / 3600)
