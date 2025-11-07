# Capítulo 1 - Exercício 14
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

nome = input("Digite o nome do produto: ")
preco_custo = float(input("Digite o preço de custo do produto: "))
preco_venda = float(input("Digite o preço de venda do produto: "))
estoque = int(input("Digite a quantidade em estoque do produto: "))

lucro_total = (preco_venda - preco_custo) * estoque

print(f"Lucro total do estoque de {nome}: R$ {lucro_total:.2f}")
