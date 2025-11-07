# Capítulo 6 - Exercício 12
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

chaves = ["chave1", "chave2", "chave3"]
valores = [1, 2, 3]

dicionario = {chaves[i]: valores[i] for i in range(len(chaves))}
print(dicionario)
