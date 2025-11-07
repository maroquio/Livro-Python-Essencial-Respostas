# Exercício 4.5 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para inserir um número e calcule o fatorial desse número.

## Solução

```python
import math

num = int(input("Digite um número: "))
fatorial = math.factorial(num)
print(f"O fatorial de {num} é {fatorial}")
```

## Explicação

Na solução deste exercício, primeiro, é solicitado ao usuário que insira um número através da função `input()`. O número inserido é convertido para um inteiro usando a função `int()`. Em seguida, a função `math.factorial()` é utilizada para calcular o fatorial do número. O resultado é então impresso na tela.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
