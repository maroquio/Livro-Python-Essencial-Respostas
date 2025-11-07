# Exercício 9.6 - Tratamento de Exceções

## Enunciado

Implemente um jogo de adivinhação em que o usuário deve acertar um número entre 1 e 10. Utilize tratamento de exceções para garantir que o usuário insira apenas números válidos.

## Solução

```python
import random

numero_secreto = random.randint(1, 10)

while True:
    try:
        palpite = int(input("Adivinhe um número entre 1 e 10: "))
        if palpite == numero_secreto:
            print("Parabéns, você acertou!")
            break
        else:
            print("Infelizmente você errou, tente novamente.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número.")
```

## Explicação

Nesta solução, inicializamos um número aleatório entre 1 e 10 chamado `numero_secreto`. Então, entramos em um laço infinito onde solicitamos ao usuário um palpite. O palpite é convertido para um inteiro e, se for igual ao `numero_secreto`, o usuário vence o jogo e o laço é interrompido. Se o palpite não for igual ao `numero_secreto`, o usuário é informado que errou e o jogo continua. Se o usuário inserir algo que não possa ser convertido para um inteiro, uma `ValueError` será lançada. Essa exceção é capturada e uma mensagem de erro é exibida, pedindo ao usuário que insira um número.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
