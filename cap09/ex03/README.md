# Exercício 9.3 - Tratamento de Exceções

## Enunciado

Implemente uma calculadora que realize operações de soma, subtração, multiplicação e divisão. Utilize tratamento de exceções para lidar com operações inválidas.

## Solução

```python
def calcular(op, num1, num2):
    try:
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return num1 / num2
        else:
            raise ValueError("Operação inválida.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except TypeError:
        print("Erro: Entrada inválida. Certifique-se de digitar um número.")

print(calcular("/", 5, 0))
```

## Explicação

A função `calcular` recebe uma operação (representada por uma string) e dois números. A operação pode ser uma das quatro operações aritméticas básicas: soma (`+`), subtração (`-`), multiplicação (`*`) ou divisão (`/`). Dependendo da operação fornecida, a função executa a operação apropriada. Se a operação fornecida não for reconhecida, uma `ValueError` é lançada com a mensagem "Operação inválida.". A função também possui tratamento de exceções para `ZeroDivisionError` (se o usuário tentar dividir por zero) e `TypeError` (se os valores fornecidos para `num1` ou `num2` não forem números).

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
