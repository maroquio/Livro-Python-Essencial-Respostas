# Exercício 6.3 - Coleções

## Enunciado

Faça um programa que use *List Comprehension* para criar uma lista com o quadrado dos números pares entre 0 e 10.

## Solução

```python
# Cria uma lista com o quadrado dos números pares entre 0 e 10
quadrados = [x**2 for x in range(11) if x % 2 == 0]

print(quadrados)
```

## Explicação

Nesta solução, usamos *list comprehension* para gerar uma lista de quadrados de todos os números pares entre 0 e 10. A condição {x \

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
