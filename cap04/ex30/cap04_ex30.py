# Capítulo 4 - Exercício 30
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

from datetime import datetime

# Define a data e hora atuais
data_hora_atual = datetime.now()

# Formata a data e hora para exibir o número da semana do ano
numero_semana_ano = data_hora_atual.strftime("%U")

print(f"A data e hora atuais são: {data_hora_atual}")
print(f"O número da semana do ano é: {numero_semana_ano}")
