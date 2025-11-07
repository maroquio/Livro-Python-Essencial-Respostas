# Capítulo 6 - Exercício 23
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import random

perguntas_respostas = {"Qual é a capital do Brasil?": "Brasília",
                       "Qual é a moeda do Japão?": "Iene",
                       "Qual é o maior planeta do sistema solar?": "Júpiter"}

pergunta = random.choice(list(perguntas_respostas.keys()))
print(pergunta)
resposta = input("Digite a sua resposta: ")

if resposta.lower() == perguntas_respostas[pergunta].lower():
    print("Resposta correta!")
else:
    print(f"Resposta incorreta. A resposta correta é: {perguntas_respostas[pergunta]}")
