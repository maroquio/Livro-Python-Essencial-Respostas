# Capítulo 4 - Exercício 29
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

from datetime import datetime

# Define a data e hora atuais
data_hora_atual = datetime.now()

# Formata a data e hora para exibir o número do dia do ano
numero_dia_ano = data_hora_atual.strftime("%j")

print(f"A data e hora atuais são: {data_hora_atual}")
print(f"O número do dia do ano é: {numero_dia_ano}")
