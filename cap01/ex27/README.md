# Exercício 1.27 - Fundamentos da Linguagem

## Enunciado

(**Difícil**) Crie um programa que peça ao usuário para digitar o valor inicial de um investimento, a taxa de juros mensal e o número de meses que o valor ficou investido. Em seguida, o programa deve calcular e mostrar o valor final do investimento, considerando o uso de juros compostos.

## Solução

```python
valor_inicial = float(input("Valor inicial do investimento (R$): "))
taxa_juros = float(input("Taxa de juros mensal (%): "))
meses = int(input("Número de meses: "))

taxa_juros /= 100
valor_final = valor_inicial * (1 + taxa_juros)**meses

print(f"Valor final do investimento: R$ {valor_final:.2f}")
```

## Explicação

Neste código, solicitamos ao usuário o valor inicial do investimento, a taxa de juros e o número de anos, e armazenamos os valores nas variáveis `valor_inicial`, `taxa_juros` e `meses`, respectivamente. Em seguida, convertemos a taxa de juros para decimal, dividindo-a por 100. Calculamos o valor final do investimento utilizando a fórmula dos juros compostos `valor_final = valor_inicial * (1 + taxa_juros)**meses`. Por fim, imprimimos o resultado formatado com duas casas decimais.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
