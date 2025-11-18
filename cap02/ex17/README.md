# Exercício 2.17 - Estruturas Condicionais

## Enunciado

Crie um programa que pergunte ao usuário sua idade e exiba uma mensagem de acordo com as seguintes regras: "Você é jovem", se a idade for menor do que 21; "Você é adulto", se a idade estiver entre 21 e 60; ou "Você é idoso", caso a idade seja superior a 60.

## Solução

```python
idade = int(input("Digite sua idade: "))

if idade < 21:
    print("Você é jovem.")
elif 21 <= idade <= 60:
    print("Você é adulto.")
else:
    print("Você é idoso.")
```

## Explicação

Neste código, pedimos ao usuário para digitar sua idade e convertemos o valor inserido para tipo `int`. Em seguida, utilizamos estruturas condicionais para verificar a faixa etária do usuário e imprimir a mensagem apropriada conforme as regras estabelecidas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
