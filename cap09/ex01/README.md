# Exercício 9.1 - Tratamento de Exceções

## Enunciado

Crie um programa que solicite ao usuário dois números inteiros e exiba a divisão do primeiro número pelo segundo. Trate possíveis exceções de divisão por zero.

## Solução

```python
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(f"Resultado: {num1 / num2}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de digitar um número inteiro.")
```

## Explicação

Nesta solução, utilizamos o bloco `try/except` para lidar com as exceções. Primeiro, solicitamos ao usuário que insira dois números inteiros (`num1` e `num2`). Em seguida, tentamos dividir `num1` por `num2` e exibimos o resultado. Se `num2` for zero, uma `ZeroDivisionError` será lançada, e o programa irá capturar essa exceção e imprimir uma mensagem de erro. Da mesma forma, se o usuário inserir algo que não seja um número inteiro, uma `ValueError` será lançada e o programa imprimirá uma mensagem de erro apropriada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
