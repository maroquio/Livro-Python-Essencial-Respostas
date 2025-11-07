# Capítulo 9 - Exercício 3
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
