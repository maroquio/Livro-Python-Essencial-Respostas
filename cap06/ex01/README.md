# Exercício 6.1 - Coleções

## Enunciado

Faça um programa que use *List Comprehension* para criar uma lista com as raízes quadradas dos números pares de 0 a 20.

## Solução

```python
import math

# Cria uma lista com as raízes quadradas dos números pares de 0 a 20
raizes = [math.sqrt(x) for x in range(21) if x % 2 == 0]

print(raizes)
```

## Explicação

Nesta solução, importamos o módulo `math` para acessar a função de raiz quadrada (`sqrt`). Em seguida, usamos *list comprehension* para gerar uma lista de raízes quadradas para todos os números pares de 0 a 20. A condição {x \

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
