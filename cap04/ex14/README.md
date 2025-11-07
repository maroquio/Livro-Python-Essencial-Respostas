# Exercício 4.14 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, mostre a posição inicial de cada palavra contida nessa frase.

## Solução

```python
frase = input("Digite uma frase: ")
palavras = frase.split()

for palavra in palavras:
    posicao_inicial = frase.find(palavra)
    print(f"A palavra '{palavra}' começa na posição {posicao_inicial}")
```

## Explicação

Neste código, solicitamos ao usuário que insira uma frase. A frase é então dividida em palavras com o método `split()`. Em seguida, iteramos sobre as palavras e, para cada palavra, encontramos sua posição inicial na frase com o método `find()`. A posição inicial de cada palavra é então impressa.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
