# Exercício 1.6 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar um número. Em seguida, o programa deve calcular e mostrar a raiz quadrada desse número.

## Solução

```python
import math

num = float(input("Digite um número: "))

raiz_quadrada = math.sqrt(num)

print(f"Raiz quadrada de {num}: {raiz_quadrada:.2f}")
```

## Explicação

O código utiliza a biblioteca *math* para calcular a raiz quadrada de um número. O número é digitado pelo usuário utilizando a função *input()*. Em seguida, é calculada a raiz quadrada do número utilizando a função *math.sqrt()*, armazenando-a na variável *raiz_quadrada*. Por fim, o *print()* é utilizado para imprimir a variável *raiz_quadrada* com duas casas decimais.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
