# Exercício 3.6 - Estruturas de Repetição

## Enunciado

Crie um programa que some e mostre todos os números ímpares de 1 a 100.

## Solução

```python
soma = 0
for i in range(1, 101):
    if i % 2 != 0:
        soma += i
print(soma)
```

## Explicação

Este código é similar ao anterior, mas a estrutura condicional {if i \

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
