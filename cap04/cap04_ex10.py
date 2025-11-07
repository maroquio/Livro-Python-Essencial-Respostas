# Capítulo 4 - Exercício 10
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import re

frase = input("Digite uma frase: ")
frase_sem_artigos = re.sub(r"\ba\b|\bo\b|\bas\b|\bos\b|\bum\b|\buns\b|\buma\b|\bumas\b", "", frase, flags=re.IGNORECASE)
print(frase_sem_artigos)
