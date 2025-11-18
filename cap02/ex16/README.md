# Exercício 2.16 - Estruturas Condicionais

## Enunciado

Crie um programa que pergunte ao usuário seu peso e sua altura e exiba uma mensagem de acordo com seu IMC (índice de massa corporal), conforme as seguintes regras: "Você está abaixo do peso", se o IMC for menor do que 18,5; "Você está com o peso normal", se o IMC estiver entre 18,5 e 24,9; "Você está com sobrepeso", se o IMC estiver entre 25 e 29,9; ou "Você está com obesidade", caso o IMC seja superior a 29,9.

## Solução

```python
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print("Você está com o peso normal.")
elif 25 <= imc <= 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
```

## Explicação

Neste código, as duas primeiras linhas solicitam ao usuário seu peso e altura, convertendo os valores inseridos para tipo `float`. Em seguida, calculamos o índice de massa corporal (IMC) dividindo o peso pela altura ao quadrado. As próximas linhas verificam a faixa de IMC e exibem a mensagem apropriada de acordo com as regras estabelecidas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
