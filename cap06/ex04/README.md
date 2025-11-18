# Exercício 6.4 - Coleções

## Enunciado

Faça um programa que use *List Comprehension* para criar uma lista com os números divisíveis por 3 ou 5 de 0 a 30.

## Solução

```python
# Cria uma lista com os números divisíveis por 3 ou 5 de 0 a 30
divisiveis = [x for x in range(31) if x % 3 == 0 or x % 5 == 0]

print(divisiveis)
```

## Explicação

Nesta solução, usamos *list comprehension* para gerar uma lista de todos os números entre 0 e 30 que são divisíveis por 3 ou 5. A condição {x \

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
