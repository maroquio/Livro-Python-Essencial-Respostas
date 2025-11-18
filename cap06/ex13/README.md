# Exercício 6.13 - Coleções

## Enunciado

Faça um programa que declare duas listas com 5 valores inteiros cada. Usando a função `zip` e *List Comprehension*, retorne uma terceira lista com a média dos elementos de mesmo índice.

## Solução

```python
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

medias = [(a+b)/2 for a, b in zip(lista1, lista2)]
print(medias)
```

## Explicação

Nesta solução, temos duas listas de números, `lista1` e `lista2`. Usamos a função `zip()` para agrupar os elementos correspondentes de `lista1` e `lista2`, criando uma lista de tuplas, em que cada tupla tem os dois valores de mesmo índice de `lista1` e `lista2`. Em seguida, usamos *list comprehension* para calcular a média de cada par de números. O resultado é uma nova lista chamada `medias`, que contém as médias dos elementos de mesmo índice das duas listas originais.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
