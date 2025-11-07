# Capítulo 6 - Exercício 28
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

def pega_palavras(texto):
    palavras = texto.split(" ")
    for palavra in palavras:
        yield palavra

texto = "Esta é uma frase de exemplo"
generator = pega_palavras(texto)
for palavra in generator:
    print(palavra)
