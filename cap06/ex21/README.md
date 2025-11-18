# Exercício 6.21 - Coleções

## Enunciado

Escreva um programa em Python que cria uma lista de *strings* com 5 nomes de frutas. Use a função `random.choice` para escolher uma fruta aleatória da lista e imprimir na tela. Teste seu programa várias vezes para verificar a aleatoriedade da escolha.

## Solução

```python
import random

lista_frutas = ["maçã", "banana", "abacaxi", "manga", "uva"]
fruta_escolhida = random.choice(lista_frutas)
print(fruta_escolhida)
```

## Explicação

Este programa começa importando o módulo `random` do Python, que fornece uma variedade de funções que geram números aleatórios de várias maneiras. Em seguida, ele define `lista_frutas`, que é uma lista de strings que representam os nomes das frutas. Depois, utiliza a função `random.choice` para escolher uma fruta aleatória da `lista_frutas` e atribuir o resultado à variável `fruta_escolhida`. Finalmente, imprime a `fruta_escolhida`. A função `random.choice` garante que cada item na lista tenha uma chance igual de ser escolhido.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
