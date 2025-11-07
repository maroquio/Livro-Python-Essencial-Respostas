# Exercício 6.25 - Coleções

## Enunciado

Desenvolva um programa que simule um sorteio de nomes para um amigo secreto. Cada pessoa só pode tirar outra pessoa uma vez e uma pessoa não pode tirar a si mesma. O programa deve continuar sorteando até que todas as pessoas tenham tirado um amigo secreto. Utilize a função `random.choice` para realizar o sorteio. As pessoas participantes são: "Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana". Ao final, o programa deve exibir quem tirou quem no amigo secreto.

## Solução

```python
import random

participantes = ['Alice', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena', 'Igor', 'Juliana']
amigo_secreto = {}

for p in participantes:
    possiveis = list(set(participantes) - set([p]) - set(amigo_secreto.values()))
    amigo_secreto[p] = random.choice(possiveis)

for p, a in amigo_secreto.items():
    print(f"{p} tirou {a}")
```

## Explicação

Nesta solução, inicialmente importamos o módulo `random`, necessário para a escolha aleatória de um amigo secreto. Criamos uma lista chamada `participantes`, que contém todos os nomes dos participantes do jogo de amigo secreto. Também definimos um dicionário vazio `amigo_secreto` que será usado para armazenar os pares de amigo secreto. No laço `for`, iteramos sobre todos os participantes. Para cada participante, criamos uma lista `possiveis` que contém todos os participantes que ainda não foram escolhidos e que não são o participante atual. A escolha do amigo secreto é feita de forma aleatória dentre os possíveis candidatos utilizando `random.choice` e a escolha é armazenada no dicionário `amigo_secreto`. Finalmente, iteramos sobre o dicionário `amigo_secreto` e mostramos todos os pares de amigo secreto.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
