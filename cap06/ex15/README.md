# Exercício 6.15 - Coleções

## Enunciado

Faça um programa que declare uma lista de 10 números inteiros e um número de referência pertencente à lista. Ao fim, retorne uma nova lista contendo os itens da lista original que tenham valor superior ao número de referência.

## Solução

```python
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_referencia = 5
nova_lista = [num for num in lista_original if num > numero_referencia]
print(nova_lista)
```

## Explicação

Este programa começa declarando uma `lista\_original` de 10 números inteiros e um `numero\_referencia` que está presente na lista. A `lista\_original` é uma lista de números de 1 a 10, e o `numero\_referencia` é 5. Em seguida, ele usa *list comprehension* para criar uma `nova\_lista` que contém apenas os números da `lista\_original` que são maiores que o `numero\_referencia`. A expressão `num for num in lista\_original if num > numero\_referencia` significa "para cada número na lista original, se o número for maior que o número de referência, adicione-o à nova lista". Ao fim, o programa imprime a `nova\_lista`, que conterá todos os números da lista original que são maiores que 5.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
