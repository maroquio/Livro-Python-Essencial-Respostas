# Capítulo 4 - Exercício 27
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

from datetime import datetime, timedelta

# Define uma data e hora específicas
data_hora_especifica = datetime(2023, 1, 1, 10, 30)

# Adiciona 2 dias e 5 horas à data e hora específicas
data_hora_futura = data_hora_especifica + timedelta(days=2, hours=5)

print(f"A data e hora específicas são: {data_hora_especifica}")
print(f"A data e hora após adicionar 2 dias e 5 horas: {data_hora_futura}")
