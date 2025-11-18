# Capítulo 1 - Exercício 27
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

valor_inicial = float(input("Valor inicial do investimento (R$): "))
taxa_juros = float(input("Taxa de juros mensal (%): "))
meses = int(input("Número de meses: "))

taxa_juros /= 100
valor_final = valor_inicial * (1 + taxa_juros)**meses

print(f"Valor final do investimento: R$ {valor_final:.2f}")
