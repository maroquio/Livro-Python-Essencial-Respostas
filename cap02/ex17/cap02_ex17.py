# Capítulo 2 - Exercício 17
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

idade = int(input("Digite sua idade: "))

if idade < 21:
    print("Você é jovem.")
elif 21 <= idade <= 60:
    print("Você é adulto.")
else:
    print("Você é idoso.")
