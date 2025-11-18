# Exercício 3.5 - Estruturas de Repetição

## Enunciado

Crie um programa que some e mostre todos os números pares de 1 a 100.

## Solução

```python
soma = 0
for i in range(1, 101):
    if i % 2 == 0:
        soma += i
print(soma)
```

## Explicação

Neste código, inicializamos a variável `soma` com zero. Em seguida, usamos um laço `for` para iterar sobre uma sequência de números de 1 a 100. Para cada número `i` na sequência, verificamos se o número é par usando a estrutura condicional {if i \

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
