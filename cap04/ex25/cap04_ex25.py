# Capítulo 4 - Exercício 25
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

from datetime import datetime, timedelta

# Obtém a data atual
data_atual = datetime.now()

# Adiciona 30 dias à data atual
data_futura = data_atual + timedelta(days=30)

print(f"A data atual é: {data_atual}")
print(f"A data após 30 dias será: {data_futura}")
