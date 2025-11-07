# Capítulo 6 - Exercício 24
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import random

opcoes = ["pedra", "papel", "tesoura"]
escolha_computador = random.choice(opcoes)
escolha_jogador = input("Digite sua escolha (pedra, papel, tesoura): ")

print(f"O computador escolheu {escolha_computador}")

if escolha_jogador == escolha_computador:
    print("Empate!")
elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
     (escolha_jogador == "papel" and escolha_computador == "pedra") or \
     (escolha_jogador == "tesoura" and escolha_computador == "papel"):
    print("Você ganhou!")
else:
    print("Você perdeu!")
