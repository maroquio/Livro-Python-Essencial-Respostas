# Capítulo 4 - Exercício 12
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

frase = input("Digite uma frase: ")

palavras = frase.split()
conta_o = sum([1 for palavra in palavras if palavra.endswith('o')])
conta_a = sum([1 for palavra in palavras if palavra.endswith('a')])

print("Palavras terminadas em 'o':", conta_o)
print("Palavras terminadas em 'a':", conta_a)
