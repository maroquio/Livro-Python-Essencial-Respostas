# Capítulo 1 - Exercício 25
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

nome = input("Digite o nome da pessoa: ")
salario = float(input("Digite o salário (R$): "))
imposto = float(input("Digite o valor do imposto (R$): "))

salario_liquido = salario - imposto

print(f"{nome} tem um salário líquido de R$ {salario_liquido:.2f}")
