# Exercício 7.6 - Arquivos, Módulos e Pacotes

## Enunciado

Crie um programa que solicite ao usuário o nome de arquivo existente na mesma pasta, copie-o para um novo arquivo mudando a extensão para ".cópia" e exiba o resultado da operação na tela.

## Solução

```python
import shutil
import os

nome_arquivo = input("Digite o nome do arquivo: ")
base = os.path.splitext(nome_arquivo)[0]
shutil.copy2(nome_arquivo, base + ".cópia")
with open(base + ".cópia", "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)
```

## Explicação

Neste código, utilizamos o módulo `shutil` do Python, que oferece uma série de operações de alto nível em arquivos. Primeiro, solicitamos ao usuário que insira o nome do arquivo. Em seguida, usamos `os.path.splitext` para separar o nome do arquivo de sua extensão. O método `shutil.copy2` é então utilizado para copiar o arquivo original para um novo arquivo com a mesma base de nome, mas com a extensão modificada para ".cópia". Finalmente, lemos e imprimimos o conteúdo do novo arquivo.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
