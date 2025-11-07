# Capítulo 2 - Exercício 10
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

temperatura = float(input("Digite a temperatura corporal: "))

if temperatura < 36:
    print("A temperatura está abaixo da faixa normal.")
elif temperatura > 37:
    print("A temperatura está acima da faixa normal.")
else:
    print("A temperatura está dentro da faixa normal.")
