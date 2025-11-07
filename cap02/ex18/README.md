# Exercício 2.18 - Estruturas Condicionais

## Enunciado

Crie um programa que peça ao usuário para digitar 5 números inteiros. O programa deve exibir uma mensagem informando se todos os números digitados são pares ou se há pelo menos um número ímpar.

## Solução

```python
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0 and num4 % 2 == 0 and num5 % 2 == 0:
    print("Todos os números são pares.")
else:
    print("Há pelo menos um número ímpar.")
```

## Explicação

Neste código, pedimos ao usuário que insira 5 números inteiros, um de cada vez. Em seguida, utilizamos uma estrutura condicional para verificar se todos os números são pares, dividindo cada um deles por 2 e verificando se o resto da divisão é igual a 0. Se todos os números forem pares, imprimimos a mensagem "Todos os números são pares". Caso contrário, imprimimos "Há pelo menos um número ímpar".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
