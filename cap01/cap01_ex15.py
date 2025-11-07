# Capítulo 1 - Exercício 15
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

valor_venda = float(input("Valor da venda: "))
desconto = float(input("Percentual de desconto: "))
imposto = float(input("Percentual do imposto: "))

valor_final = valor_venda * (1 - desconto / 100) * (1 + imposto / 100)

print(f"Preço final da venda: R$ {valor_final:.2f}")
