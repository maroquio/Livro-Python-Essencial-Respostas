# Exercício 6.8 - Coleções

## Enunciado

Faça um programa que peça ao usuário para digitar uma lista de números e que use mapeamento (`map`) para retornar uma nova lista com os quadrados de cada número.

## Solução

```python
numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
quadrados = list(map(lambda n: n**2, numeros))
```

## Explicação

Nesse código, primeiro solicitamos ao usuário que insira uma lista de números separados por espaço. Usamos a função `split()` para dividir a entrada do usuário em uma lista de *strings*. Em seguida, usamos a função `map()` com `int` como função de mapeamento para converter cada *string* em um número inteiro. Em seguida, aplicamos a função `map()` novamente para obter o quadrado de cada número na lista. A função lambda `lambda n: n**2` é usada como a função de mapeamento para calcular o quadrado de cada número.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
