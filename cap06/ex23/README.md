# Exercício 6.23 - Coleções

## Enunciado

Neste exercício você vai criar um jogo de perguntas e respostas. As perguntas e suas respectivas respostas devem ser armazenadas em um dicionário, onde as chaves são as perguntas e os valores são as respostas. Escreva um programa que escolhe uma pergunta aleatória do dicionário e a imprime na tela. O usuário deve então tentar responder à pergunta e o programa deve informar se a resposta está correta ou não.

## Solução

```python
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
```

## Explicação

Este programa também começa importando o módulo `random`. Em seguida, ele define um dicionário `perguntas_respostas`, onde as chaves são as perguntas e os valores são as respostas correspondentes. Em seguida, usa `random.choice` para escolher uma pergunta aleatória do dicionário. Como `random.choice` não pode ser usado diretamente em dicionários, primeiro convertemos as chaves do dicionário em uma lista usando `list()`. A pergunta escolhida é então impressa e o programa solicita ao usuário que digite a resposta. A resposta do usuário é comparada com a resposta correta do dicionário (ambas convertidas para letras minúsculas para evitar problemas de diferenciação de maiúsculas e minúsculas). Se a resposta estiver correta, o programa imprime uma mensagem de sucesso. Se a resposta estiver incorreta, ele imprime a resposta correta.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
