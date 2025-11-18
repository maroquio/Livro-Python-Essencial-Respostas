# Capítulo 7 - Exercício 10
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import os
import zipfile

os.mkdir("Textos")
for i in range(1, 4):
    with open(f"Textos/arquivo{i}.txt", "w") as f:
        f.write("Python Essencial")

with zipfile.ZipFile("Textos.zip", "w") as myzip:
    for root, dirs, files in os.walk("Textos"):
        for file in files:
            myzip.write(os.path.join(root, file))
