# Exercício 6.17 - Coleções

## Enunciado

Faça um programa que declare uma lista com ao menos 10 números inteiros, com pelo menos 3 deles repetidos. Em seguida, converta essa lista para um conjunto, visando eliminar os itens repetidos, converta de volta para uma lista, e mostre o resultado na tela.

## Solução

```python
lista = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
conjunto = set(lista)
lista = list(conjunto)
print(lista)
```

## Explicação

Nesta solução, começamos com uma lista de números que contém valores repetidos. Usamos a função `set()` para converter essa lista em um conjunto, que automaticamente remove valores repetidos. Em seguida, convertemos o conjunto de volta para uma lista com a função `list()`. Ao final, imprimimos a lista resultante.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
