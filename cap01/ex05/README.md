# Exercício 1.5 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar três números e imprima a soma do dobro de cada um deles.

## Solução

```python
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

soma_dobro = 2*num1 + 2*num2 + 2*num3

print(f"Soma do dobro: {soma_dobro}")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite três números, que são armazenados nas variáveis `num1`, `num2` e `num3`. Em seguida, é calculada a soma do dobro desses três números e ela é armazenada na variável `soma_dobro`, que é obtida multiplicando cada número por dois e somando-os. Por fim, o `print()` é utilizado para imprimir a variável `soma_dobro`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
