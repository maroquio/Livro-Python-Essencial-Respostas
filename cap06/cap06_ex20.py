# Capítulo 6 - Exercício 20
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

jogadores = {}
while True:
    numero = int(input("Digite o número da camisa: "))
    if numero == -1:
        break
    nome = input("Digite o nome do jogador: ")
    jogadores[numero] = nome

for numero, nome in sorted(jogadores.items()):
    print(f"Camisa {numero}: {nome}")
