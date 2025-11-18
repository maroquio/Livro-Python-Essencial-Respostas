# Capítulo 1 - Exercício 17
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

v_inicial = float(input("Digite a velocidade inicial: "))
v_final = float(input("Digite a velocidade final: "))
tempo = float(input("Digite o tempo de transição (em segundos): "))

aceleracao = (v_final - v_inicial) / tempo

print(f"Aceleração: {aceleracao:.2f} m/s²")
