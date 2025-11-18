# Exercício 1.9 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar dois números quaisquer. Em seguida, o programa deve calcular e mostrar a potência do primeiro número pelo segundo.

## Solução

```python
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

potencia = num1 ** num2

print(f"{num1} elevado a {num2}: {potencia}")
```

## Explicação

O código utiliza a função *input()* para solicitar que o usuário digite dois números, que são armazenados nas variáveis *num1* e *num2*. Em seguida, é calculada a potência do primeiro número pelo segundo número, que é armazenada na variável *potencia*, obtida elevando o primeiro número ao segundo. Por fim, a função *print()* é utilizada para imprimir a variável *potencia* com uma mensagem formatada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
