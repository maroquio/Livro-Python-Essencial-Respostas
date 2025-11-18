# Exercício 6.24 - Coleções

## Enunciado

Desenvolva um jogo de "Pedra, Papel e Tesoura". Crie uma lista com as opções "pedra", "papel" e "tesoura". Utilize a função `random.choice` para que o computador escolha aleatoriamente entre as opções. O usuário deve inserir a sua escolha e, em seguida, o programa deve comparar a escolha do usuário com a do computador para determinar o vencedor de acordo com as regras do jogo.

## Solução

```python
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
```

## Explicação

Neste programa, definimos uma lista de opções para o jogo "Pedra, Papel e Tesoura". O programa então usa a função `random.choice` para escolher uma das opções para o computador. Em seguida, ele solicita que o jogador insira sua escolha. O programa então imprime a escolha do computador e compara as escolhas do jogador e do computador para determinar o vencedor. O operador `elif` é usado para verificar as condições de vitória para o jogador. Se nenhuma dessas condições for atendida, o programa assume que o jogador perdeu.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
