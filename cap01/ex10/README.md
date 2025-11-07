# Exercício 1.10 - Fundamentos da Linguagem

## Enunciado

(**Difícil**) Crie um programa que peça ao usuário para digitar três números (A, B e C). Em seguida, o programa deve calcular e mostrar os valores das raízes da seguinte equação, usando a fórmula de Bhaskara: [ Ax^2 + Bx + C = 0]

## Solução

```python
import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    raiz = -b / (2 * a)
    print(f"A equação possui uma raiz real: {raiz:.2f}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")
```

## Explicação

O código utiliza a biblioteca *math* para calcular as raízes de uma equação do segundo grau. Os valores de A, B e C são digitados pelo usuário utilizando a função *input()*. Em seguida, é calculado o valor de delta utilizando a fórmula de Bhaskara, armazenando-o na variável *delta*. A partir desse valor, é verificado o número de raízes da equação e os valores das raízes são armazenados nas variáveis *raiz1* e *raiz2* (quando existem duas raízes). Por fim, a função *print()* é utilizada para imprimir uma mensagem formatada com as raízes obtidas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
