# Exercício 2.20 - Estruturas Condicionais

## Enunciado

Crie um programa que peça ao usuário para digitar um número de CPF e verifique se ele é válido. Considere que, para um CPF ser válido, ele deve ter exatamente 11 dígitos inteiros (use a função len(cpf) para obter o tamanho e a função cpf.isdigit para saber se é um número inteiro).

## Solução

```python
cpf = input("Digite um número de CPF: ")

if len(cpf) == 11 and cpf.isdigit():
    print("O CPF é válido.")
else:
    print("O CPF é inválido.")
```

## Explicação

Neste código, pedimos ao usuário que insira um número de CPF. Em seguida, verificamos se o CPF possui exatamente 11 caracteres e se todos os caracteres são dígitos usando a função `isdigit()`. Caso ambas as condições sejam verdadeiras, imprimimos a mensagem "O CPF é válido". Caso contrário, imprimimos "O CPF é inválido".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
