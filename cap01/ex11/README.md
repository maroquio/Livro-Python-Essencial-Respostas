# Exercício 1.11 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar o raio de um círculo. Em seguida, o programa deve calcular e mostrar a área e o comprimento do círculo.

## Solução

```python
import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * raio ** 2
comprimento = 2 * math.pi * raio

print(f"Área do círculo: {area:.2f}")
print(f"Comprimento do círculo: {comprimento:.2f}")
```

## Explicação

O código utiliza a biblioteca `math` para calcular a área e o comprimento de um círculo. O raio do círculo é digitado pelo usuário utilizando a função `input()`. Em seguida, são calculados a área e o comprimento do círculo utilizando as fórmulas correspondentes da geometria e impressos utilizando o `print()`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
