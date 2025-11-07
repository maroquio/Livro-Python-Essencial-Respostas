# Capítulo 4 - Exercício 28
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

from datetime import datetime, timedelta

# Define a data e hora atuais
data_hora_atual = datetime.now()

# Define uma data e hora futura
data_hora_futura = datetime(2025, 1, 1, 10, 30)

# Verifica se a data e hora atuais são anteriores à data e hora futura
eh_antes = data_hora_atual < data_hora_futura

print(f"A data e hora atuais são: {data_hora_atual}")
print(f"A data e hora futura são: {data_hora_futura}")
print(f"A data e hora atuais são anteriores à data e hora futura? {eh_antes}")
