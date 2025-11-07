# Capítulo 1 - Exercício 30
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)
diferenca1 = conjunto1.difference(conjunto2)
diferenca2 = conjunto2.difference(conjunto1)

print("União dos conjuntos:", uniao)
print("Interseção dos conjuntos:", intersecao)
print("Diferença entre conjunto1 e conjunto2:", diferenca1)
print("Diferença entre conjunto2 e conjunto1:", diferenca2)
