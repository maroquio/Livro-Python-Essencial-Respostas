# Exercício 3.9 - Estruturas de Repetição

## Enunciado

Crie um programa que calcule e mostre todos os números divisíveis por 3 ou 5 de 1 a 100.

## Solução

```python
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
```

## Explicação

Neste programa, o laço `for` itera sobre uma sequência de números de 1 a 100. A estrutura condicional `if` verifica se o número atual `i` é divisível por 3 ou 5. A operação {i \

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
