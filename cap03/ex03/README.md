# Exercício 3.3 - Estruturas de Repetição

## Enunciado

Crie um programa que mostre todos os números ímpares de 1 a 100.

## Solução

```python
for i in range(1, 101):
    if i % 2 != 0:
        print(i)
```

## Explicação

Este código é quase idêntico ao anterior, exceto que a condição `if` verifica se o número é ímpar. Se o resto da divisão de `i` por 2 for diferente de zero ({i \

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
