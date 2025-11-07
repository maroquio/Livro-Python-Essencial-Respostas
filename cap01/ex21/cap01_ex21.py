# Capítulo 1 - Exercício 21
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

distancia = float(input("Digite a distância percorrida (m): "))
tempo = float(input("Digite o tempo gasto (s): "))
aceleracao = float(input("Digite a aceleração (m/s²): "))

v_inicial = (distancia - 0.5 * aceleracao * tempo**2) / tempo
v_final = v_inicial + aceleracao * tempo

print(f"Velocidade inicial: {v_inicial:.2f} m/s")
print(f"Velocidade final: {v_final:.2f} m/s")
