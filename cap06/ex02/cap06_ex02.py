# Capítulo 6 - Exercício 2
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

# Solicita ao usuário para digitar uma frase
frase = input("Digite uma frase: ")

# Cria uma lista com as palavras que contêm a letra "a", substituindo a letra por "o"
palavras_modificadas = [palavra.replace("a", "o") for palavra in frase.split() if "a" in palavra]

print(palavras_modificadas)
