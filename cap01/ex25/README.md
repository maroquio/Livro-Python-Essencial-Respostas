# Exercício 1.25 - Fundamentos da Linguagem

## Enunciado

Crie um programa que leia o nome, o salário e o valor do imposto de uma pessoa como entrada e imprima, ao fim, uma saída no seguinte formato: "Fulano tem um salário líquido de R\$ 1.800,00.". Observe a formatação do salário.

## Solução

```python
nome = input("Digite o nome da pessoa: ")
salario = float(input("Digite o salário (R$): "))
imposto = float(input("Digite o valor do imposto (R$): "))

salario_liquido = salario - imposto

print(f"{nome} tem um salário líquido de R$ {salario_liquido:.2f}")
```

## Explicação

Neste código, solicitamos ao usuário o nome da pessoa, o salário e o valor do imposto, e armazenamos os valores nas variáveis `nome`, `salario` e `imposto`, respectivamente. Em seguida, calculamos o salário líquido subtraindo o imposto do salário, ou seja, `salario_liquido =` `salario - imposto`. Por fim, imprimimos o resultado formatado com duas casas decimais e o nome da pessoa.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
