# Capítulo 2 - Exercício 25
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

a = float(input("Insira o número a: "))
b = float(input("Insira o número b: "))
op = input("Insira a operação aritmética (+, -, * ou /): ")
result = None

match op:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a * b
    case "/":
        if b != 0:
            result = a / b
        else:
            result = "Divisão por zero não permitida"
    case _:
        result = "Operação inválida"

print(f"Resultado: {result}")
