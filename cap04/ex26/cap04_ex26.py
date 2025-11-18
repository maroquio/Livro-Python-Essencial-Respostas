# Capítulo 4 - Exercício 26
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

from datetime import datetime, timedelta

# Obtém a hora atual
hora_atual = datetime.now()

# Subtrai 2 horas da hora atual
hora_anterior = hora_atual - timedelta(hours=2)

print(f"A hora atual é: {hora_atual}")
print(f"A hora 2 horas atrás era: {hora_anterior}")
