# Exercício 3.13 - Estruturas de Repetição

## Enunciado

Crie um programa que calcule e mostre a tabuada de um número digitado pelo usuário.

## Solução

```python
num = int(input("Digite um número para ver a sua tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

## Explicação

O programa começa lendo um número inteiro do usuário. Depois, usa um laço `for` para iterar de 1 a 10. Para cada número `i` na sequência, ele imprime o produto do número digitado pelo usuário e `i`. Isso produz a tabuada do número digitado pelo usuário.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
