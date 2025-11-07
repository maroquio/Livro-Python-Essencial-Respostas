# Capítulo 9 - Exercício 2
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

def calcular_media(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        print("Erro: Não é possível calcular a média de uma lista vazia.")
    except TypeError:
        print("Erro: Todos os elementos da lista devem ser numéricos.")

lista = [1, 2, 3, 4, 5]
print(calcular_media(lista))
