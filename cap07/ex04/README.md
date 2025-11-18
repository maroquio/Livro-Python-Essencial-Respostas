# Exercício 7.4 - Arquivos, Módulos e Pacotes

## Enunciado

Crie um programa que solicite ao usuário o nome de um arquivo e que renomeie esse arquivo adicionando a palavra "renomeado" ao nome existente, mantendo sua extensão.

## Solução

```python
import os
nome_arquivo = input("Digite o nome do arquivo: ")
base = os.path.splitext(nome_arquivo)[0]
extensao = os.path.splitext(nome_arquivo)[1]
os.rename(nome_arquivo, f"{base}_renomeado{extensao}")
```

## Explicação

Este programa utiliza o módulo `os` do Python para interagir com o sistema operacional. A função `os.path.splitext` é usada para separar o nome do arquivo e sua extensão. A função `os.rename` é usada para renomear o arquivo, adicionando "_renomeado" ao nome original do arquivo e mantendo a extensão original.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
