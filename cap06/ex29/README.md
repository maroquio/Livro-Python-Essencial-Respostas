# Exercício 6.29 - Coleções

## Enunciado

Crie um *generator* que receba uma lista de números e retorne, a cada iteração, o quadrado do próximo número da lista. Use esse *generator* para imprimir os quadrados dos números de uma lista de 1 a 10.

## Solução

```python
def quadrados(lista):
    for num in lista:
        yield num ** 2

lista = list(range(1, 11))
generator = quadrados(lista)
for quadrado in generator:
    print(quadrado)
```

## Explicação

Este *generator* recebe uma lista de números como argumento e gera o quadrado de cada número um a um. Ao fim, estamos usando a função `quadrados` para imprimir os quadrados dos números de 1 a 10.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
