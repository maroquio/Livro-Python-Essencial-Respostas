# Exercício 2.1 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se um número é par ou ímpar.

## Solução

```python
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

## Explicação

Neste código, solicitamos ao usuário que digite um número e armazenamos o valor na variável `numero`. Em seguida, verificamos se o número é par ou ímpar utilizando a operação módulo (`\%`). Se o resto da divisão do número por 2 for igual a 0, o número é par; caso contrário, é ímpar. Por fim, imprimimos o resultado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
