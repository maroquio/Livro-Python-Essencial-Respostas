# Exercício 1.15 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar o valor total de uma venda, o percentual de desconto aplicado e o percentual de imposto cobrado. Ao fim, o programa deve mostrar o preço final da mercadoria, sendo que o imposto é cobrado sobre o valor com desconto.

## Solução

```python
valor_venda = float(input("Valor da venda: "))
desconto = float(input("Percentual de desconto: "))
imposto = float(input("Percentual do imposto: "))

valor_final = valor_venda * (1 - desconto / 100) * (1 + imposto / 100)

print(f"Preço final da venda: R$ {valor_final:.2f}")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite o valor de uma venda e os percentuais de desconto e de imposto, que são armazenados nas variáveis `valor_venda`, `desconto` e `imposto`, respectivamente. Em seguida, é calculado o preço final da venda, aplicando-se o desconto e o imposto sobre o preço original que, por sua vez, é impresso utilizando o `print()`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
