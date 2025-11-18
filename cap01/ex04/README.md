# Exercício 1.4 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar seu peso e sua altura. Em seguida, calcule o índice de massa corporal (IMC) e imprima o resultado. A fórmula do IMC é: [IMC = peso / altura^2]

## Solução

```python
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"IMC: {imc:.2f}")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite o peso e a altura, que são armazenados nas variáveis `peso` e `altura`. Em seguida, é calculado o IMC utilizando a fórmula e armazenado na variável `imc`. Por fim, o `print()` é utilizado para imprimir a variável `imc` com duas casas decimais.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
