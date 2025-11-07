# Exercício 4.15 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, mostre quantas vezes cada palavra aparece nessa frase.

## Solução

```python
# Solução 1
frase = input("Digite uma frase: ")
palavras = frase.split()
frequencia_palavras = {}

for palavra in palavras:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1

for palavra, frequencia in frequencia_palavras.items():
    print(f"A palavra '{palavra}' aparece {frequencia} vez(es) na frase.")

# Solução 2
from collections import Counter

frase = input("Digite uma frase: ")
palavras = frase.split()
contador = Counter(palavras)

for palavra, frequencia in contador.items():
    print(f"A palavra '{palavra}' aparece {frequencia} vez(es)")
```

## Explicação

Na primeira solução, o programa primeiro pede ao usuário para digitar uma frase usando a função `input()`. Em seguida, ele divide a frase em palavras individuais usando o método `split()`. Depois disso, um dicionário chamado `frequencia_palavras` é criado para armazenar cada palavra e sua respectiva frequência. O programa então percorre cada palavra na lista de palavras. Se a palavra já está no dicionário, ele aumenta o contador de frequência para essa palavra em 1. Se não está, ele adiciona a palavra ao dicionário com um contador de frequência de 1. Por fim, o programa percorre cada item no dicionário `frequencia_palavras` e imprime a palavra e sua frequência.

Na segunda solução, mais compacta, importamos a classe `Counter` da biblioteca `collections`. Em seguida, pedimos ao usuário que insira uma frase, que dividimos em palavras com o método `split()`. A classe `Counter` é usada para contar a frequência de cada palavra na lista de palavras. Em seguida, iteramos sobre o objeto `Counter` e imprimimos a frequência de cada palavra.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
