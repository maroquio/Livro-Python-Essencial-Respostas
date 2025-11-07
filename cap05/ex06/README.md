# Exercício 5.6 - Funções

## Enunciado

Crie um programa que declare uma lista chamada `idades` com 5 números inteiros. Logo em seguida, crie uma função chamada `adicionar` que receba uma lista como parâmetro e que adicione um novo elemento qualquer a essa lista. Feito isso, chame a função `adicionar` passando a lista `idades` como argumento. Por fim, após a chamada da função, mostre a lista *idades* para verificar se o elemento foi adicionado corretamente.

## Solução

```python
idades = [20, 25, 30, 35, 40]

def adicionar(lista):
    lista.append(45)

adicionar(idades)
print(idades)
```

## Explicação

Este código declara uma lista `idades` com cinco números inteiros. Então, define uma função `adicionar()` que aceita uma lista como parâmetro e adiciona um novo elemento a essa lista. Em seguida, chamamos a função `adicionar()` passando a lista `idades` como argumento. Por fim, imprimimos a lista `idades` para verificar se o novo elemento foi adicionado corretamente.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
