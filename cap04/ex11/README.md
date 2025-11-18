# Exercício 4.11 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, fatie a frase em *substrings* de 6 caracteres e mostre-as uma por linha.

## Solução

```python
frase = input("Digite uma frase: ")

for i in range(0, len(frase), 6):
    print(frase[i:i+6])
```

## Explicação

Este código pede ao usuário que insira uma frase. A frase é então fatiada em substrings de 6 caracteres cada uma. O loop `for` passa por cada índice da frase de 6 em 6 caracteres, e a cada iteração imprime uma substring da frase.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
