# Capítulo 9 - Exercício 8
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
