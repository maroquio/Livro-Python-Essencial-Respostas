# Capítulo 2 - Exercício 23
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

emocao = input("Insira uma emoção (feliz, triste, nervoso): ").lower()

match emocao:
    case "feliz":
        print(":)")
    case "triste":
        print(":(")
    case "nervoso":
        print(":/")
    case _:
        print("Emoção não reconhecida")
