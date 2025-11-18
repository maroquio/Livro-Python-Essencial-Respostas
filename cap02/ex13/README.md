# Exercício 2.13 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se um número inteiro digitado pelo usuário é divisível por outro número inteiro também digitado pelo usuário.

## Solução

```python
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 % num2 == 0:
    print(f"{num1} é divisível por {num2}.")
else:
    print(f"{num1} não é divisível por {num2}.")
```

## Explicação

Neste código, pedimos ao usuário que digite dois números inteiros, armazenando-os nas variáveis `num1` e `num2`. Usamos a estrutura condicional `if` para verificar se o primeiro número é divisível pelo segundo número, ou seja, se o resto da divisão de `num1` por `num2` é igual a 0. Se for verdadeiro, `num1` é divisível por `num2` e imprimimos a mensagem correspondente. Caso contrário, `num1` não é divisível por `num2` e imprimimos a devida mensagem.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
