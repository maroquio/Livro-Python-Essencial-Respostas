# Capítulo 9 - Exercício 1
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(f"Resultado: {num1 / num2}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de digitar um número inteiro.")
