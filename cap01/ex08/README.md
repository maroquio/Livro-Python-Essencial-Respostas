# Exercício 1.8 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar um ângulo entre 0 e 360 graus. Em seguida, o programa deve calcular e mostrar o seno, cosseno e tangente desse número.

## Solução

```python
import math

num = float(input("Digite um número: "))

seno = math.sin(num)
cosseno = math.cos(num)
tangente = math.tan(num)

print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")
```

## Explicação

O código utiliza a biblioteca *math* para calcular o seno, cosseno e tangente de um número. O número é digitado pelo usuário utilizando a função *input()*. Em seguida, são calculados os valores do seno, cosseno e tangente utilizando as respectivas funções da biblioteca *math*. Por fim, os valores são impressos utilizando a função *print()*.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
