# Exercício 2.14 - Estruturas Condicionais

## Enunciado

Crie um programa que pergunte ao usuário seu salário e exiba uma mensagem de "Alto salário" se o salário for maior do que R\$10.000,00, ou "Baixo salário" caso contrário.

## Solução

```python
salario = float(input("Digite seu salário: "))

if salario > 10000:
    print("Alto salário.")
else:
    print("Baixo salário.")
```

## Explicação

Neste código, pedimos ao usuário que digite seu salário, armazenando-o na variável `salario`. Usamos a estrutura condicional `if` para verificar se o salário é maior do que 10000. Se for verdadeiro, imprimimos a mensagem "Alto salário". Caso contrário, imprimimos a mensagem "Baixo salário".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
