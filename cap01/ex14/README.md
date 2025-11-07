# Exercício 1.14 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar o nome, o preço de custo, o preço de venda e a quantidade em estoque de determinado produto. Em seguida, o programa deve calcular e mostrar o lucro que esse produto pode gerar se todo o estoque for vendido.

## Solução

```python
nome = input("Digite o nome do produto: ")
preco_custo = float(input("Digite o preço de custo do produto: "))
preco_venda = float(input("Digite o preço de venda do produto: "))
estoque = int(input("Digite a quantidade em estoque do produto: "))

lucro_total = (preco_venda - preco_custo) * estoque

print(f"Lucro total do estoque de {nome}: R$ {lucro_total:.2f}")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite o nome, preço de custo, preço de venda e quantidade em estoque de um produto, que são armazenados nas variáveis `nome`, `preco_custo`, `preco_venda` e `estoque`, respectivamente. Em seguida, é calculado o lucro total que o estoque desse produto pode gerar se todos os produtos forem vendidos, utilizando a fórmula (preço de venda - preço de custo) * quantidade em estoque e impresso utilizando o `print()`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
