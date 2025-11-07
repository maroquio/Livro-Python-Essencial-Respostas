# Capítulo 5 - Exercício 7
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

def contagemRegressiva(n):
    if n >= 0:
        print(n)
        contagemRegressiva(n-1)
    else:
        print("Contagem regressiva finalizada!")

contagemRegressiva(5)
