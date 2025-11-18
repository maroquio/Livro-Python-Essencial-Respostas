# Exercício 7.10 - Arquivos, Módulos e Pacotes

## Enunciado

Faça um programa que crie um diretório chamado "Textos" e que, dentro desse diretório, crie 3 arquivos com os nomes "arquivo1.txt", "arquivo2.txt" e "arquivo3.txt", todos contendo o texto "Python Essencial". Em seguida, o programa deve criar um arquivo compactado (.zip) contendo o diretório "Textos".

## Solução

```python
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
```

## Explicação

Neste código, criamos um diretório chamado "Textos" e, em seguida, três arquivos texto dentro desse diretório, cada um contendo a *string* "Python Essencial". Em seguida, utilizamos o módulo `zipfile` para criar um arquivo *zip* chamado "Textos.zip". Usamos a função `os.walk` para percorrer todos os arquivos no diretório "Textos" e adicioná-los ao arquivo *zip* usando o método `write` do objeto `ZipFile`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
