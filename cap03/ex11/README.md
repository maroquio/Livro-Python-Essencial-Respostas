# Exercício 3.11 - Estruturas de Repetição

## Enunciado

Crie um programa que calcule e mostre todos os números entre 1 e 100 que possuem raiz quadrada exata.

## Solução

```python
import math

for i in range(1, 101):
    raiz = math.sqrt(i)
    if raiz == int(raiz):
        print(i)
```

## Explicação

Este programa imprime todos os números entre 1 e 100 que têm uma raiz quadrada exata. Primeiro, importamos o módulo `math` do Python, que contém a função `sqrt` usada para calcular a raiz quadrada. Em seguida, o programa entra em um laço `for` que varia de 1 a 100 (inclusive). Para cada número neste intervalo, o programa calcula a raiz quadrada do número. Se a raiz quadrada é igual à sua parte inteira (isto é, se a raiz quadrada é um número inteiro), então o número tem uma raiz quadrada exata e o programa imprime o número.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
