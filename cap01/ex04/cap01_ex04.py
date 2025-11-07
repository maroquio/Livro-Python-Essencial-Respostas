# Capítulo 1 - Exercício 4
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"IMC: {imc:.2f}")
