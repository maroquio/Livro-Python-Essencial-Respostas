# Exercício 2.19 - Estruturas Condicionais

## Enunciado

Crie um programa que gere um número aleatório entre 1 e 10 e peça para o usuário tentar adivinhar o número. Em caso de erro, o programa deve informar se o número digitado pelo usuário é maior ou menor do que o número gerado (use `import random` no início e `random.randint(1, 10)` para obter o número aleatório).

## Solução

```python
import random

numero_aleatorio = random.randint(1, 10)
tentativa = int(input("Tente adivinhar o número entre 1 e 10: "))

if tentativa == numero_aleatorio:
    print("Parabéns, você acertou!")
elif tentativa > numero_aleatorio:
    print("O número é menor.")
else:
    print("O número é maior.")
```

## Explicação

Neste código, importamos o módulo `random` para gerar um número aleatório entre 1 e 10. Em seguida, pedimos ao usuário que insira uma tentativa para adivinhar o número gerado. Utilizamos estruturas condicionais para verificar se o usuário acertou o número ou se o número inserido é maior ou menor que o número gerado, imprimindo a mensagem apropriada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
