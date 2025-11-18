# Exercício 3.20 - Estruturas de Repetição

## Enunciado

Crie um programa que calcule e mostre o fatorial de todos os números de 1 a *n*, onde *n* é digitado pelo usuário.

## Solução

```python
n = int(input("Digite um número: "))
for i in range(1, n + 1):
    fatorial = 1
    for j in range(1, i + 1):
        fatorial *= j
    print(f"Fatorial de {i} é {fatorial}")
```

## Explicação

Este programa imprime o fatorial de todos os números de 1 até `n`, onde `n` é fornecido pelo usuário. O programa primeiro lê o valor de `n`. Em seguida, ele entra em um laço `for` que vai de 1 até `n` (inclusive). Para cada número `i` no intervalo, o programa calcula o fatorial de `i`. Ele faz isso entrando em outro laço `for` que vai de 1 até `i` (inclusive) e multiplica o valor atual do fatorial por cada número neste intervalo. Finalmente, o programa imprime o fatorial de `i`. Este processo é repetido para cada número de 1 a `n`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
