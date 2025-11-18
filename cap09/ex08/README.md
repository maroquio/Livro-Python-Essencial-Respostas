# Exercício 9.8 - Tratamento de Exceções

## Enunciado

Implemente um jogo de adivinhação em que o usuário deve acertar uma palavra secreta. Utilize tratamento de exceções para garantir que o usuário insira apenas letras do alfabeto.

## Solução

```python
def adivinha_palavra(palavra_secreta):
    try:
        while True:
            palavra = input("Adivinhe a palavra secreta: ")
            if not palavra.isalpha():
                raise ValueError("Sua entrada deve ser apenas letras.")
            if palavra == palavra_secreta:
                print("Parabéns, você acertou a palavra secreta!")
                break
    except ValueError as e:
        print("Erro:", e)

adivinha_palavra("python")
```

## Explicação

A função `adivinha_palavra` recebe uma palavra secreta e pede ao usuário para adivinhar a palavra. Se a entrada do usuário não for composta apenas por letras, lançamos uma exceção `ValueError`. Se o usuário adivinhar a palavra corretamente, saímos do laço. Caso contrário, o laço continua até que a palavra seja adivinhada corretamente.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
