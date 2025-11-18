# Exercício 2.2 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se um número digitado pelo usuário é positivo, negativo ou zero.

## Solução

```python
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
```

## Explicação

Neste código, solicitamos ao usuário que digite um número e armazenamos o valor na variável `numero`. Em seguida, verificamos se o número é positivo, negativo ou zero usando estruturas condicionais (`if`, `elif` e `else`). Por fim, imprimimos o resultado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
