# Capítulo 6 - Exercício 10
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

palavras = input("Digite uma lista de palavras separadas por vírgula: ").split(",")
comprimentos = list(map(len, palavras))
print(comprimentos)
