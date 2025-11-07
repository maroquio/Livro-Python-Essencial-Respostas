# Capítulo 5 - Exercício 10
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

def transformarLista(lista, funcao):
    return [funcao(x) for x in lista]

def porExtenso(num):
    numeros = {
        0: "zero",
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove"
    }
    return numeros.get(num)

lista_original = [1, 2, 3, 4, 5]
lista_transformada = transformarLista(lista_original, porExtenso)
print(lista_transformada)
