# Capítulo 2 - Exercício 24
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

faixa = input("Insira sua faixa etária (criança, adolescente, adulto): ").lower()

match faixa:
    case "criança":
        print("Sugerido: Filme infantil")
    case "adolescente":
        print("Sugerido: Filme de ação")
    case "adulto":
        print("Sugerido: Filme de drama")
    case _:
        print("Faixa etária não reconhecida")
