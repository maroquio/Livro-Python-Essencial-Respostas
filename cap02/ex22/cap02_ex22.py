# Capítulo 2 - Exercício 22
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

clima = input("Insira a descrição do clima (ensolarado, chuvoso, nublado etc.): ").lower()

match clima:
    case "ensolarado":
        print("Use óculos de sol")
    case "chuvoso":
        print("Leve um guarda-chuva")
    case "nublado":
        print("Leve um casaco leve")
    case _:
        print("Clima não reconhecido")
